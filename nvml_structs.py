from ctypes import Structure, c_char, c_int, c_uint
import ctypes
import nvml_defines as defines
import nvml_enums as enums

nvmlVgpuInstance_t = c_int


class nvmlPciInfo_t(Structure):
    """
    PCI information about a GPU device.
    """
    _fields_ = [
        ("busIdLegacy", c_char * defines.NVML_DEVICE_PCI_BUS_ID_BUFFER_V2_SIZE),
        ("domain", c_uint),             # The PCI domain on which the device's bus resides, 0 to 0xffffffff
        ("bus", c_uint),                # The bus on which the device resides, 0 to 0xff
        ("device", c_uint),             # The device's id on the bus, 0 to 31
        ("pciDeviceId", c_uint),        # The combined 16-bit device id and 16-bit vendor id
        ("pciSubSystemId", c_uint),     # The 32-bit Sub System Device ID
        ("busId", c_char * defines.NVML_DEVICE_PCI_BUS_ID_BUFFER_SIZE)  # The tuple domain:bus:device.function PCI identifier (&amp; NULL terminator)
    ]


class nvmlUtilization_t(Structure):
    """
    Utilization information for a device.
    Each sample period may be between 1 second and 1/6 second, depending on the product being queried.
    """
    _fields_ = [
        ("gpu", c_uint),    # Percent of time over the past sample period during which one or more kernels was executing on the GPU
        ("memory", c_uint)  # Percent of time over the past sample period during which global (device) memory was being read or written
    ]


class nvmlMemory_t(Structure):
    """
    Memory allocation information for a device.
    """
    _fields_ = [
        ("total", c_uint),  # Total installed FB memory (in bytes)
        ("free", c_uint),   # Unallocated FB memory (in bytes)
        ("used", c_uint)    # Allocated FB memory (in bytes). Note that the driver/GPU always sets aside a small amount of memory for bookkeeping
    ]


class nvmlUnitInfo_t(Structure):
    _fields_ = [
        ("name", c_char * 96),
        ("id", c_char * 96),
        ("serial", c_char * 96),
        ("firmwareVersion", c_char * 96)
    ]


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
        ("smUtil", nvmlValue_t),            # SM (3D/Compute) Util Value
        ("memUtil", nvmlValue_t),           # Frame Buffer Memory Util Value
        ("encUtil", nvmlValue_t),           # Encoder Util Value
        ("decUtil", nvmlValue_t)            # Decoder Util Value
    ]


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


class nvmlLedState_t(Structure):
    _fields_ = [
        ("cause", c_char * 256),
        ("color", enums.nvmlLedColor_t)
    ]


class nvmlDevice(Structure):
    pass


nvmlDevice_t = ctypes.POINTER(nvmlDevice)
