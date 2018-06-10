from ctypes import c_int
from enum import IntEnum


nvmlEncoderType_t = c_int
nvmlLedColor_t = c_int
nvmlBrandType_t = c_int
nvmlTemperatureSensors_t = c_int
nvmlClockType_t = c_int
nvmlClockId_t = c_int
nvmlPstates_t = c_int
nvmlGpuOperationMode_t = c_int
nvmlFieldValue_t = c_int


class nvmlLedColor(IntEnum):
    GREEN = 0
    AMBER = 1


# Clock types. All speeds are in Mhz.
class nvmlClockType(IntEnum):
    NVML_CLOCK_GRAPHICS = 0     # Graphics clock domain
    NVML_CLOCK_SM = 1           # SM clock domain
    NVML_CLOCK_MEM = 2          # Memory clock domain
    NVML_CLOCK_VIDEO = 3        # Video encoder/decoder clock domain


# Clock Ids. These are used in combination with nvmlClockType_t to specify a single clock value.
class nvmlClockId(IntEnum):
    NVML_CLOCK_ID_CURRENT = 0               # Current actual clock value
    NVML_CLOCK_ID_APP_CLOCK_TARGET = 1      # Target application clock
    NVML_CLOCK_ID_APP_CLOCK_DEFAULT = 2     # Default application clock target
    NVML_CLOCK_ID_CUSTOMER_BOOST_MAX = 3    # OEM-defined maximum clock rate


# Allowed PStates.
class nvmlPstates(IntEnum):
    NVML_PSTATE_0 = 0           # Performance state 0 -- Maximum Performance
    NVML_PSTATE_1 = 1           # Performance state 1
    NVML_PSTATE_2 = 2           # Performance state 2
    NVML_PSTATE_3 = 3           # Performance state 3
    NVML_PSTATE_4 = 4           # Performance state 4
    NVML_PSTATE_5 = 5           # Performance state 5
    NVML_PSTATE_6 = 6           # Performance state 6
    NVML_PSTATE_7 = 7           # Performance state 7
    NVML_PSTATE_8 = 8           # Performance state 8
    NVML_PSTATE_9 = 9           # Performance state 9
    NVML_PSTATE_10 = 10         # Performance state 10
    NVML_PSTATE_11 = 11         # Performance state 11
    NVML_PSTATE_12 = 12         # Performance state 12
    NVML_PSTATE_13 = 13         # Performance state 13
    NVML_PSTATE_14 = 14         # Performance state 14
    NVML_PSTATE_15 = 15         # Performance state 15 -- Minimum Performance
    NVML_PSTATE_UNKNOWN = 32    # Unknown performance state


# GPU Operation Mode
# GOM allows to reduce power usage and optimize GPU throughput by disabling GPU features.
# Each GOM is designed to meet specific user needs.
class nvmlGpuOperationMode(IntEnum):
    NVML_GOM_ALL_ON = 0     # Everything is enabled and running at full speed
    NVML_GOM_COMPUTE = 1    # Designed for running only compute tasks. Graphics operations are not allowed
    NVML_GOM_LOW_DP = 2     # Designed for running graphics applications that don't require high bandwidth double precision


# Represents type of encoder for capacity can be queried
class nvmlEncoderType(IntEnum):
    NVML_ENCODER_QUERY_H264 = 0
    NVML_ENCODER_QUERY_HEVC = 1


# The Brand of the GPU
class nvmlBrandType(IntEnum):
    NVML_BRAND_UNKNOWN = 0
    NVML_BRAND_QUADRO = 1
    NVML_BRAND_TESLA = 2
    NVML_BRAND_NVS = 3
    NVML_BRAND_GRID = 4
    NVML_BRAND_GEFORCE = 5
    NVML_BRAND_TITAN = 6

    __names__ = [
        "Unknown",
        "Quadro",
        "Tesla",
        "NVS",
        "GRID",
        "GeForce",
        "Titan"
    ]

    @property
    def brandName(self):
        return self.__names__[self.value]


# Temperature sensors.
class nvmlTemperatureSensors(IntEnum):
    NVML_TEMPERATURE_GPU = 0
