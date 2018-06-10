from enum import IntEnum


class NVMLError(Exception):
    pass


class NVMLErrorUninitialized(NVMLError):
    pass


class NVMLErrorInvalidArgument(NVMLError):
    pass


class NVMLErrorNotSupported(NVMLError):
    pass


class NVMLErrorNoPermission(NVMLError):
    pass


class NVMLErrorAlreadyInitialized(NVMLError):
    pass


class NVMLErrorNotFound(NVMLError):
    pass


class NVMLErrorInsufficientSize(NVMLError):
    pass


class NVMLErrorInsufficientPower(NVMLError):
    pass


class NVMLErrorDriverNotLoaded(NVMLError):
    pass


class NVMLErrorTimeout(NVMLError):
    pass


class NVMLErrorIRQIssue(NVMLError):
    pass


class NVMLErrorLibraryNotFound(NVMLError):
    pass


class NVMLErrorFunctionNotFound(NVMLError):
    pass


class NVMLErrorCorruptedInfoRom(NVMLError):
    pass


class NVMLErrorGPUIsLost(NVMLError):
    pass


class NVMLErrorResetRequired(NVMLError):
    pass


class NVMLErrorOSBlockedRequest(NVMLError):
    pass


class NVMLErrorLibRMVersionMismatch(NVMLError):
    pass


class NVMLErrorGPUInUse(NVMLError):
    pass


class NVMLErrorInsufficientMemory(NVMLError):
    pass


class NVMLErrorNoData(NVMLError):
    pass


class NVMLErrorVGPUECCNotSupported(NVMLError):
    pass


class NVMLErrorUnknownError(NVMLError):
    pass


class nvmlReturn(IntEnum):
    NVML_SUCCESS = 0                            # The operation was successful
    NVML_ERROR_UNINITIALIZED = 1                # NVML was not first initialized with nvmlInit()
    NVML_ERROR_INVALID_ARGUMENT = 2             # A supplied argument is invalid
    NVML_ERROR_NOT_SUPPORTED = 3                # The requested operation is not available on target device
    NVML_ERROR_NO_PERMISSION = 4                # The current user does not have permission for operation
    NVML_ERROR_ALREADY_INITIALIZED = 5          # Deprecated: Multiple initializations are now allowed through ref counting
    NVML_ERROR_NOT_FOUND = 6                    # A query to find an object was unsuccessful
    NVML_ERROR_INSUFFICIENT_SIZE = 7            # An input argument is not large enough
    NVML_ERROR_INSUFFICIENT_POWER = 8           # A device's external power cables are not properly attached
    NVML_ERROR_DRIVER_NOT_LOADED = 9            # NVIDIA driver is not loaded
    NVML_ERROR_TIMEOUT = 10                     # User provided timeout passed
    NVML_ERROR_IRQ_ISSUE = 11                   # NVIDIA Kernel detected an interrupt issue with a GPU
    NVML_ERROR_LIBRARY_NOT_FOUND = 12           # NVML Shared Library couldn't be found or loaded
    NVML_ERROR_FUNCTION_NOT_FOUND = 13          # Local version of NVML doesn't implement this function
    NVML_ERROR_CORRUPTED_INFOROM = 14           # infoROM is corrupted
    NVML_ERROR_GPU_IS_LOST = 15                 # The GPU has fallen off the bus or has otherwise become inaccessible
    NVML_ERROR_RESET_REQUIRED = 16              # The GPU requires a reset before it can be used again
    NVML_ERROR_OPERATING_SYSTEM = 17            # The GPU control device has been blocked by the operating system/cgroups
    NVML_ERROR_LIB_RM_VERSION_MISMATCH = 18     # RM detects a driver/library version mismatch
    NVML_ERROR_IN_USE = 19                      # An operation cannot be performed because the GPU is currently in use
    NVML_ERROR_MEMORY = 20                      # Insufficient memory
    NVML_ERROR_NO_DATA = 21                     # No data
    NVML_ERROR_VGPU_ECC_NOT_SUPPORTED = 22      # The requested vgpu operation is not available on target device, becasue ECC is enabled
    NVML_ERROR_UNKNOWN = 999                    # An internal driver error occurred

    __exceptions__ = {
        1: NVMLErrorUninitialized,
        2: NVMLErrorInvalidArgument,
        3: NVMLErrorNotSupported,
        4: NVMLErrorNoPermission,
        5: NVMLErrorAlreadyInitialized,
        6: NVMLErrorNotFound,
        7: NVMLErrorInsufficientSize,
        8: NVMLErrorInsufficientPower,
        9: NVMLErrorDriverNotLoaded,
        10: NVMLErrorTimeout,
        11: NVMLErrorIRQIssue,
        12: NVMLErrorLibraryNotFound,
        13: NVMLErrorFunctionNotFound,
        14: NVMLErrorCorruptedInfoRom,
        15: NVMLErrorGPUIsLost,
        16: NVMLErrorResetRequired,
        17: NVMLErrorOSBlockedRequest,
        18: NVMLErrorLibRMVersionMismatch,
        19: NVMLErrorGPUInUse,
        20: NVMLErrorInsufficientMemory,
        21: NVMLErrorNoData,
        22: NVMLErrorVGPUECCNotSupported,
        999: NVMLErrorUnknownError,
    }

    @classmethod
    def test(cls, errno):
        if errno != cls.NVML_SUCCESS:
            raise cls.__exceptions__[errno]
