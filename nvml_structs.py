from ctypes import Structure, c_char, c_uint
import ctypes
import nvml_defines as defines
import nvml_enums as enums

nvmlVgpuTypeId_t = c_uint
nvmlVgpuInstance_t = c_uint


class nvmlPciInfo_t(Structure):
    """
    PCI information about a GPU device.
    """
    _fields_ = [
        ("busIdLegacy", c_char * defines.NVML_DEVICE_PCI_BUS_ID_BUFFER_V2_SIZE),    # The legacy tuple domain:bus:device.function PCI identifier (&amp; NULL terminator)
        ("domain", c_uint),                                                         # The PCI domain on which the device's bus resides, 0 to 0xffffffff
        ("bus", c_uint),                                                            # The bus on which the device resides, 0 to 0xff
        ("device", c_uint),                                                         # The device's id on the bus, 0 to 31
        ("pciDeviceId", c_uint),                                                    # The combined 16-bit device id and 16-bit vendor id
        ("pciSubSystemId", c_uint),                                                 # The 32-bit Sub System Device ID
        ("busId", c_char * defines.NVML_DEVICE_PCI_BUS_ID_BUFFER_SIZE)              # The tuple domain:bus:device.function PCI identifier (&amp; NULL terminator)
    ]


class nvmlPciInfo:
    def __init__(self, pciInfo: nvmlPciInfo_t):
        self.busIdLegacy = pciInfo.busIdLegacy.decode()
        self.busId = pciInfo.busId.decode() or self.busIdLegacy
        self.domain = pciInfo.domain
        self.bus = pciInfo.bus
        self.device = pciInfo.device
        self.pciDeviceId = pciInfo.pciDeviceId
        self.pciSubSystemId = pciInfo.pciSubSystemId

    def __repr__(self):
        return f"<nvmlPciInfo({self.busId})>"


class nvmlUtilization_t(Structure):
    """
    Utilization information for a device.
    Each sample period may be between 1 second and 1/6 second, depending on the product being queried.
    """
    _fields_ = [
        ("gpu", c_uint),    # Percent of time over the past sample period during which one or more kernels was executing on the GPU
        ("memory", c_uint)  # Percent of time over the past sample period during which global (device) memory was being read or written
    ]


class nvmlUtilization:
    def __init__(self, utilization: nvmlUtilization_t):
        self.gpu = utilization.gpu
        self.memory = utilization.memory


class nvmlMemory_t(Structure):
    """
    Memory allocation information for a device.
    """
    _fields_ = [
        ("total", c_uint),  # Total installed FB memory (in bytes)
        ("free", c_uint),   # Unallocated FB memory (in bytes)
        ("used", c_uint)    # Allocated FB memory (in bytes). Note that the driver/GPU always sets aside a small amount of memory for bookkeeping
    ]


class nvmlMemory:
    def __init__(self, memory: nvmlMemory_t):
        self.total = memory.total
        self.free = memory.free
        self.used = memory.used


class nvmlUnitInfo_t(Structure):
    _fields_ = [
        ("name", c_char * 96),
        ("id", c_char * 96),
        ("serial", c_char * 96),
        ("firmwareVersion", c_char * 96)
    ]


class nvmlUnitInfo:
    def __init__(self, unitInfo: nvmlUnitInfo_t):
        self.name = unitInfo.name.decode()
        self.id = unitInfo.id.decode()
        self.serial = unitInfo.serial.decode()
        self.firmwareVersion = unitInfo.firmwareVersion.decode()


class nvmlProcessInfo_t(Structure):
    _fields_ = [
        ("pid", ctypes.c_uint),
        ("usedGpuMemory", ctypes.c_ulonglong)
    ]


class nvmlProcessInfo:
    def __init__(self, processInfo: nvmlProcessInfo_t):
        self.pid = processInfo.pid
        self.usedGpuMemory = (
            None
            if processInfo.usedGpuMemory == defines.NVML_VALUE_NOT_AVAILABLE
            else processInfo.usedGpuMemory)

    def __repr__(self):
        return f"<nvmlProcessInfo(pid={self.pid}, usedGpuMemory={self.usedGpuMemory})>"


class nvmlValue_t(ctypes.Union):
    _fields_ = [
        ("dVal", ctypes.c_double),
        ("uiVal", ctypes.c_uint),
        ("ulVal", ctypes.c_ulong),
        ("ullVal", ctypes.c_ulonglong),
        ("sllVal", ctypes.c_longlong)
    ]


# Structure to store Utilization Value and vgpuInstance
class nvmlVgpuInstanceUtilizationSample_t(Structure):
    _fields_ = [
        ("vgpuInstance", nvmlVgpuInstance_t),   # vGPU Instance
        ("timeStamp", ctypes.c_ulonglong),      # CPU Timestamp in microseconds
        ("smUtil", nvmlValue_t),                # SM (3D/Compute) Util Value
        ("memUtil", nvmlValue_t),               # Frame Buffer Memory Util Value
        ("encUtil", nvmlValue_t),               # Encoder Util Value
        ("decUtil", nvmlValue_t)                # Decoder Util Value
    ]


# Structure to store Utilization Value, vgpuInstance and subprocess information
class nvmlVgpuProcessUtilizationSample_t(Structure):
    _fields_ = [
        ("vgpuInstance", nvmlVgpuInstance_t),                                   # vGPU Instance
        ("pid", ctypes.c_uint),                                                 # PID of process running within the vGPU VM
        ("processName", ctypes.c_char * defines.NVML_VGPU_NAME_BUFFER_SIZE),    # Name of process running within the vGPU VM
        ("timeStamp", ctypes.c_ulonglong),                                      # CPU Timestamp in microseconds
        ("smUtil", nvmlValue_t),                                                # SM (3D/Compute) Util Value
        ("memUtil", nvmlValue_t),                                               # Frame Buffer Memory Util Value
        ("encUtil", nvmlValue_t),                                               # Encoder Util Value
        ("decUtil", nvmlValue_t)                                                # Decoder Util Value
    ]


# Structure to store utilization value and process Id
class nvmlProcessUtilizationSample_t(Structure):
    _fields_ = [
        ("pid", ctypes.c_uint),             # PID of process running within the vGPU VM
        ("timeStamp", ctypes.c_ulonglong),  # CPU Timestamp in microseconds
        ("smUtil", ctypes.c_uint),            # SM (3D/Compute) Util Value
        ("memUtil", ctypes.c_uint),           # Frame Buffer Memory Util Value
        ("encUtil", ctypes.c_uint),           # Encoder Util Value
        ("decUtil", ctypes.c_uint)            # Decoder Util Value
    ]


class nvmlProcessUtilizationSample:
    def __init__(self, processUtilizationSample: nvmlProcessUtilizationSample_t):
        self.pid = processUtilizationSample.pid
        self.timeStamp = processUtilizationSample.timeStamp
        self.smUtil = processUtilizationSample.smUtil
        self.memUtil = processUtilizationSample.memUtil
        self.encUtil = processUtilizationSample.encUtil
        self.decUtil = processUtilizationSample.decUtil

    def __repr__(self):
        return (
            f"<nvmlProcessUtilizationSample(pid={self.pid}, "
            f"smUtil={self.smUtil}, memUtil={self.memUtil}, "
            f"encUtil={self.encUtil}, decUtil={self.decUtil})>")


# Struct to hold encoder session data
class nvmlEncoderSessionInfo_t(Structure):
    _fields_ = [
        ("sessionId", ctypes.c_uint),               # Unique session ID
        ("pid", ctypes.c_uint),                     # Owning process ID
        ("vgpuInstance", nvmlVgpuInstance_t),       # Owning vGPU instance ID (only valid on vGPU hosts, otherwise zero)
        ("codecType", enums.nvmlEncoderType_t),     # Video encoder type
        ("hResolution", ctypes.c_uint),             # Current encode horizontal resolution
        ("vResolution", ctypes.c_uint),             # Current encode vertical resolution
        ("averageFps", ctypes.c_uint),              # Moving average encode frames per second
        ("averageLatency", ctypes.c_uint)           # Moving average encode latency in microseconds
    ]


class nvmlEncoderSessionInfo:
    def __init__(self, encoderSessionInfo: nvmlEncoderSessionInfo_t):
        self.sessionId = encoderSessionInfo.sessionId
        self.pid = encoderSessionInfo.pid
        self.vgpuInstance = encoderSessionInfo.vgpuInstance
        self.codecType = enums.nvmlEncoderType(encoderSessionInfo.codecType)
        self.hResolution = encoderSessionInfo.hResolution
        self.vResolution = encoderSessionInfo.vResolution
        self.averageFps = encoderSessionInfo.averageFps
        self.averageLatency = encoderSessionInfo.averageLatency


class nvmlLedState_t(Structure):
    _fields_ = [
        ("cause", c_char * 256),
        ("color", enums.nvmlLedColor_t)
    ]


class nvmlLedState:
    def __init__(self, ledState: nvmlLedState_t):
        self.cause = ledState.cause.decode()
        self.color = enums.nvmlLedColor(ledState.color)


class nvmlDevice(Structure):
    pass


nvmlDevice_t = ctypes.POINTER(nvmlDevice)
