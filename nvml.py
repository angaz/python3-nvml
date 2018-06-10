import threading
from ctypes import (
    CDLL, byref, c_uint, c_char_p, c_ulonglong, create_string_buffer)
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

    def call(self, fn_name, *args, checkReturn=True):
        fn = self.get_fn_pointer(fn_name)
        result = fn(*args)
        if checkReturn:
            errors.nvmlReturn.test(result)
        return errors.nvmlReturn(result)

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
        name = create_string_buffer(defines.NVML_DEVICE_NAME_BUFFER_SIZE)
        self.call(
            "nvmlDeviceGetName",
            device, name, c_uint(defines.NVML_DEVICE_NAME_BUFFER_SIZE))
        return name.value.decode()

    def nvmlDeviceGetBrand(self, device):
        brand = enums.nvmlBrandType_t()
        self.call("nvmlDeviceGetBrand", device, byref(brand))
        return enums.nvmlBrandType(brand.value)

    def nvmlDeviceGetIndex(self, device):
        index = c_uint()
        self.call("nvmlDeviceGetIndex", device, byref(index))
        return index.value

    def nvmlDeviceGetSerial(self, device):
        serial = create_string_buffer(defines.NVML_DEVICE_SERIAL_BUFFER_SIZE)
        self.call(
            "nvmlDeviceGetSerial",
            device, serial, c_uint(defines.NVML_DEVICE_SERIAL_BUFFER_SIZE))
        return serial.value.decode()

    def nvmlDeviceGetUUID(self, device):
        uuid = create_string_buffer(defines.NVML_DEVICE_UUID_BUFFER_SIZE)
        self.call(
            "nvmlDeviceGetUUID",
            device, uuid, c_uint(defines.NVML_DEVICE_UUID_BUFFER_SIZE))
        return uuid.value.decode()

    def nvmlDeviceGetPciInfo(self, device):
        pciInfo = structs.nvmlPciInfo_t()
        self.call("nvmlDeviceGetPciInfo", device, byref(pciInfo))
        return structs.nvmlPciInfo(pciInfo)

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

    def nvmlDeviceGetComputeRunningProcesses(self, device: structs.nvmlDevice_t, countOnly=False):
        """
        Get information about processes with a compute context on a device
        """
        count = c_uint(0)
        result = self.call(
            "nvmlDeviceGetComputeRunningProcesses",
            device, byref(count), None,
            checkReturn=False)

        if countOnly:
            if result == errors.nvmlReturn.NVML_SUCCESS:
                return count.value
            else:
                raise errors.nvmlReturn.test(result)

        if result == errors.nvmlReturn.NVML_SUCCESS:
            return []
        if result == errors.nvmlReturn.NVML_ERROR_INSUFFICIENT_SIZE:
            count.value = count.value * 2 + 5
            procs = (structs.nvmlProcessInfo_t * count.value)()

            self.call(
                "nvmlDeviceGetComputeRunningProcesses",
                device, byref(count), procs)

            return [
                structs.nvmlProcessInfo(procs[i])
                for i in range(count.value)
            ]
        else:
            errors.nvmlReturn.test(result)

    def nvmlDeviceGetProcessUtilization(self, device: structs.nvmlDevice_t, lastSeenTimeStamp=0, countOnly=False):
        processSamplesCount = c_uint(0)
        c_lastSeenTimeStamp = c_ulonglong(lastSeenTimeStamp)

        result = self.call(
            "nvmlDeviceGetProcessUtilization",
            device, None, byref(processSamplesCount), c_lastSeenTimeStamp,
            checkReturn=False)

        if countOnly:
            if result == errors.nvmlReturn.NVML_SUCCESS:
                return processSamplesCount.value
            else:
                raise errors.nvmlReturn.test(result)

        if result == errors.nvmlReturn.NVML_SUCCESS:
            return []
        if result == errors.nvmlReturn.NVML_ERROR_INSUFFICIENT_SIZE:
            processSamplesCount.value = processSamplesCount.value * 2 + 5
            procs = (structs.nvmlProcessUtilizationSample_t * processSamplesCount.value)()

            self.call(
                "nvmlDeviceGetProcessUtilization",
                device, procs, byref(processSamplesCount), c_lastSeenTimeStamp)

            return [
                structs.nvmlProcessUtilizationSample(procs[i])
                for i in range(processSamplesCount.value)
            ]
        else:
            errors.nvmlReturn.test(result)

    def nvmlDeviceGetEncoderSessions(self, device: structs.nvmlDevice_t, countOnly=False):
        """
        Retrieves information about active encoder sessions on a target device.
        """
        sessionCount = c_uint(0)
        result = self.call(
            "nvmlDeviceGetEncoderSessions",
            device, byref(sessionCount), None,
            checkReturn=False)

        if countOnly:
            if result == errors.nvmlReturn.NVML_SUCCESS:
                return sessionCount.value
            else:
                raise errors.nvmlReturn.test(result)

        if result == errors.nvmlReturn.NVML_SUCCESS:
            return []
        if result == errors.nvmlReturn.NVML_ERROR_INSUFFICIENT_SIZE:
            sessionCount.value = sessionCount.value * 2 + 5
            procs = (structs.nvmlEncoderSessionInfo_t * sessionCount.value)()

            self.call(
                "nvmlDeviceGetEncoderSessions",
                device, byref(sessionCount), procs)

            return [
                structs.nvmlProcessInfo(procs[i])
                for i in range(sessionCount.value)
            ]
        else:
            errors.nvmlReturn.test(result)


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
        self._brand = None
        self._pciInfo = None

    def __repr__(self):
        return f"<Nvidia GPU(index={self.index}, name={self.name})>"

    @property
    def index(self):
        if self._index is None:
            self._index = self.nvml.deviceGetIndex(self.deviceHandle)
        return self._index

    @property
    def serial(self):
        if self._serial is None:
            self._serial = self.nvml.deviceGetSerial(self.deviceHandle)
        return self._serial

    @property
    def uuid(self):
        if self._uuid is None:
            self._uuid = self.nvml.deviceGetUUID(self.deviceHandle)
        return self._uuid

    @property
    def pciInfo(self):
        if self._pciInfo is None:
            self._pciInfo = self.nvml.deviceGetPciInfo(self.deviceHandle)
        return self._pciInfo

    @property
    def name(self):
        if self._name is None:
            self._name = self.nvml.deviceGetName(self.deviceHandle)
        return self._name

    @property
    def brand(self):
        if self._brand is None:
            self._brand = self.nvml.deviceGetBrand(self.deviceHandle)
        return self._brand

    def getUtilizationRates(self):
        return self.nvml.deviceGetUtilizationRates(self.deviceHandle)

    def getEncoderCapacity(self, encoderQueryType: enums.nvmlEncoderType):
        return self.nvml.deviceGetEncoderCapacity(self.deviceHandle, encoderQueryType)

    def getEncoderStats(self):
        return self.nvml.deviceGetEncoderStats(self.deviceHandle)

    def getComputeRunningProcesses(self, countOnly=False):
        return self.nvml.deviceGetComputeRunningProcesses(self.deviceHandle, countOnly)

    def getProcessUtilization(self, lastSeenTimeStamp=0):
        return self.nvml.deviceGetProcessUtilization(self.deviceHandle, lastSeenTimeStamp)

    def getEncoderSessions(self, countOnly=False):
        return self.nvml.deviceGetEncoderSessions(self.deviceHandle, countOnly)


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

    def deviceGetBrand(self, device):
        return self.__nvml.nvmlDeviceGetBrand(device)

    def deviceGetIndex(self, device):
        return self.__nvml.nvmlDeviceGetIndex(device)

    def deviceGetSerial(self, device):
        return self.__nvml.nvmlDeviceGetSerial(device)

    def deviceGetUUID(self, device):
        return self.__nvml.nvmlDeviceGetUUID(device)

    def deviceGetPciInfo(self, device):
        return self.__nvml.nvmlDeviceGetPciInfo(device)

    def deviceGetUtilizationRates(self, device):
        return self.__nvml.nvmlDeviceGetUtilizationRates(device)

    def deviceGetEncoderCapacity(self, device: structs.nvmlDevice_t, encoderQueryType: enums.nvmlEncoderType):
        return self.__nvml.nvmlDeviceGetEncoderCapacity(device, encoderQueryType)

    def deviceGetEncoderStats(self, device: structs.nvmlDevice_t):
        return self.__nvml.nvmlDeviceGetEncoderStats(device)

    def deviceGetComputeRunningProcesses(self, device: structs.nvmlDevice_t, countOnly=False):
        return self.__nvml.nvmlDeviceGetComputeRunningProcesses(device, countOnly)

    def deviceGetProcessUtilization(self, device: structs.nvmlDevice_t, lastSeenTimeStamp=0):
        return self.__nvml.nvmlDeviceGetProcessUtilization(device, lastSeenTimeStamp)

    def deviceGetEncoderSessions(self, device: structs.nvmlDevice_t, countOnly=False):
        return self.__nvml.nvmlDeviceGetEncoderSessions(device, countOnly)

    def getAllGPUs(self):
        return [
            GPU(self, index=index)
            for index in range(self.deviceGetCount())
        ]
