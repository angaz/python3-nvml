from ctypes import c_int
from enum import IntEnum


nvmlEncoderType_t = c_int
nvmlLedColor_t = c_int


class nvmlLedColor(IntEnum):
    GREEN = 0
    AMBER = 1


class nvmlClockType(IntEnum):
    NVML_CLOCK_GRAPHICS = 0     # Graphics clock domain
    NVML_CLOCK_SM = 1           # SM clock domain
    NVML_CLOCK_MEM = 2          # Memory clock domain
    NVML_CLOCK_VIDEO = 3        # Video encoder/decoder clock domain


# Represents type of encoder for capacity can be queried
class nvmlEncoderType(IntEnum):
    NVML_ENCODER_QUERY_H264 = 0
    NVML_ENCODER_QUERY_HEVC = 1
