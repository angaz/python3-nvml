import threading
from ctypes import CDLL, byref, c_uint, c_char_p, create_string_buffer
from sys import platform

import nvml_errors as errors
import nvml_enums as enums
import nvml_structs as structs
import nvml_defines as defines

libLoadLock = threading.Lock()


class NVMLLib:
    __nvml_lib = None
    __nvml_fn_pointers = {}

    def get_fn_pointer(self, fn_name):
        if fn_name in self.__nvml_fn_pointers:
            return self.__nvml_fn_pointers[fn_name]

        libLoadLock.acquire()
        try:
            if self.__nvml_lib is None:
                raise errors.NVMLErrorUninitialized
            try:
                fn_pointer = getattr(self.__nvml_lib, fn_name)
                self.__nvml_fn_pointers[fn_name] = fn_pointer
                return fn_pointer
            except AttributeError:
                raise errors.NVMLErrorFunctionNotFound
        finally:
            libLoadLock.release()

    def call(self, fn_name, *args):
        fn = self.get_fn_pointer(fn_name)
        result = fn(*args)
        errors.nvmlReturn.test(result)
        return result

    def __init__(self):
        if self.__nvml_lib is None:
            libLoadLock.acquire()

            try:
                if self.__nvml_lib is None:
                    try:
                        if platform == "linux":
                            self.__nvml_lib = CDLL("libnvidia-ml.so.1")
                        elif platform[:3] == "win":
                            raise NotImplementedError
                    except OSError:
                        raise errors.NVMLErrorLibraryNotFound
            finally:
                libLoadLock.release()

    def nvmlShutdown(self):
        self.call("nvmlShutdown")

    def nvmlInit(self):
        self.call("nvmlInit_v2")

    def nvmlDeviceGetCount(self):
        c_count = c_uint()
        self.call("nvmlDeviceGetCount_v2", byref(c_count))
        return c_count.value

    def nvmlDeviceGetHandleByIndex(self, index):
        c_index = c_uint(index)
        device = structs.nvmlDevice_t()
        self.call("nvmlDeviceGetHandleByIndex_v2", c_index, byref(device))
        return device

    def nvmlDeviceGetHandleBySerial(self, serial):
        c_serial = c_char_p(serial)
        device = structs.nvmlDevice_t()
        self.call("nvmlDeviceGetHandleBySerial", c_serial, byref(device))
        return device

    def nvmlDeviceGetHandleByUUID(self, uuid):
        c_uuid = c_char_p(uuid)
        device = structs.nvmlDevice_t()
        self.call("nvmlDeviceGetHandleByUUID", c_uuid, byref(device))
        return device

    def nvmlDeviceGetHandleByPciBusId(self, pciBusId):
        c_busId = c_char_p(pciBusId)
        device = structs.nvmlDevice_t()
        self.call("nvmlDeviceGetHandleByPciBusId_v2", c_busId, byref(device))
        return device

    def nvmlDeviceGetName(self, device):
        c_name = create_string_buffer(defines.NVML_DEVICE_NAME_BUFFER_SIZE)
        self.call(
            "nvmlDeviceGetName",
            device, c_name, c_uint(defines.NVML_DEVICE_NAME_BUFFER_SIZE))
        return c_name.value.decode()

    def nvmlDeviceGetIndex(self, device):
        c_index = c_uint()
        self.call("nvmlDeviceGetIndex", device, byref(c_index))
        return c_index.value

    def nvmlDeviceGetSerial(self, device):
        c_serial = create_string_buffer(defines.NVML_DEVICE_SERIAL_BUFFER_SIZE)
        self.call(
            "nvmlDeviceGetSerial",
            device, c_serial, c_uint(defines.NVML_DEVICE_SERIAL_BUFFER_SIZE))
        return c_serial.value.decode()

    def nvmlDeviceGetUtilizationRates(self, device):
        utilization = structs.nvmlUtilization_t()
        self.call("nvmlDeviceGetUtilizationRates", device, byref(utilization))
        return structs.nvmlUtilization(utilization)

    def nvmlDeviceGetEncoderUtilization(self, device):
        samplingPeriodUs = c_uint()
        utilization = c_uint()
        self.call("nvmlDeviceGetEncoderUtilization", device, byref(utilization), byref(samplingPeriodUs))
        return utilization.value, samplingPeriodUs.value

    def nvmlDeviceGetEncoderCapacity(self, device: structs.nvmlDevice_t, encoderQueryType: enums.nvmlEncoderType):
        """
        Retrieves the current capacity of the device's encoder, as a percentage of maximum encoder capacity with valid values in the range 0-100.
        For Maxwell &tm; or newer fully supported devices.
        """
        c_encoderQueryType = enums.nvmlEncoderType_t(encoderQueryType)
        encoderCapacity = c_uint()
        self.call("nvmlDeviceGetEncoderCapacity", device, c_encoderQueryType, byref(encoderCapacity))
        return encoderCapacity.value

    def nvmlDeviceGetEncoderStats(self, device: structs.nvmlDevice_t):
        """
        Retrieves the current encoder statistics for a given device.
        For Maxwell &tm; or newer fully supported devices.
        """
        sessionCount = c_uint()
        averageFps = c_uint()
        averageLatency = c_uint()
        self.call("nvmlDeviceGetEncoderStats", device, byref(sessionCount), byref(averageFps), byref(averageLatency))
        return sessionCount.value, averageFps.value, averageLatency.value


class GPU:
    def __init__(
            self, nvml,
            deviceHandle=None, index=None, serial=None, uuid=None, pciBusId=None):
        self.nvml = nvml
        # assert (handle or index or serial or uuid or pciBusId) is not None
        self.deviceHandle = deviceHandle or (
            nvml.deviceGetHandleByIndex(index) if index is not None else
            nvml.deviceGetHandleBySerial(serial) if serial is not None else
            nvml.deviceGetHandleByUUID(uuid) if uuid is not None else
            nvml.deviceGetHandleByPciBusId(pciBusId)
        )

        # Identifiers
        self._index = index
        self._serial = serial
        self._uuid = uuid
        self._pciBusId = pciBusId

        self._name = None

    def __repr__(self):
        return f"<Nvidia GPU(index={self.index}, name={self.name})>"

    @property
    def index(self):
        if self._index is None:
            self._index = self.nvml.deviceGetIndex(self.deviceHandle)
        return self._index

    @property
    def name(self):
        if self._name is None:
            self._name = self.nvml.deviceGetName(self.deviceHandle)
        return self._name

    def getUtilizationRates(self):
        return self.nvml.deviceGetUtilizationRates(self.deviceHandle)

    def getEncoderCapacity(self, encoderQueryType: enums.nvmlEncoderType):
        return self.nvml.deviceGetEncoderCapacity(self.deviceHandle, encoderQueryType)

    def getEncoderStats(self):
        return self.nvml.deviceGetEncoderStats(self.deviceHandle)


class NVML:
    __nvml = NVMLLib()

    def __init__(self):
        self.__nvml.nvmlInit()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def deviceGetCount(self):
        return self.__nvml.nvmlDeviceGetCount()

    def deviceGetHandleByIndex(self, index):
        return self.__nvml.nvmlDeviceGetHandleByIndex(index)

    def deviceGetHandleBySerial(self, serial):
        return self.__nvml.nvmlDeviceGetHandleBySerial(serial)

    def deviceGetHandleByUUID(self, uuid):
        return self.__nvml.nvmlDeviceGetHandleByUUID(uuid)

    def deviceGetHandleByPciBusId(self, pciBusId):
        return self.__nvml.nvmlDeviceGetHandleByPciBusId(pciBusId)

    def deviceGetName(self, device):
        return self.__nvml.nvmlDeviceGetName(device)

    def deviceGetIndex(self, device):
        return self.__nvml.nvmlDeviceGetIndex(device)

    def deviceGetUtilizationRates(self, device):
        return self.__nvml.nvmlDeviceGetUtilizationRates(device)

    def deviceGetEncoderCapacity(self, device: structs.nvmlDevice_t, encoderQueryType: enums.nvmlEncoderType):
        return self.__nvml.nvmlDeviceGetEncoderCapacity(device, encoderQueryType)

    def deviceGetEncoderStats(self, device: structs.nvmlDevice_t):
        return self.__nvml.nvmlDeviceGetEncoderStats(device)

    def getAllGPUs(self):
        return [
            GPU(self, index=index)
            for index in range(self.deviceGetCount())
        ]
