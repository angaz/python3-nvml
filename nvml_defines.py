NVML_VALUE_NOT_AVAILABLE = -1
NVML_DEVICE_PCI_BUS_ID_BUFFER_SIZE = 32
NVML_DEVICE_PCI_BUS_ID_BUFFER_V2_SIZE = 16
NVML_NVLINK_MAX_LINKS = 6
# NVML_TOPOLOGY_CPU = NVML_TOPOLOGY_NODE
NVML_MAX_PHYSICAL_BRIDGE = 128
nvmlFlagDefault = 0
nvmlFlagForce = 1

NVML_FI_DEV_ECC_CURRENT = 1         # Current ECC mode. 1=Active. 0=Inactive
NVML_FI_DEV_ECC_PENDING = 2         # Pending ECC mode. 1=Active. 0=Inactive

# ECC Count Totals
NVML_FI_DEV_ECC_SBE_VOL_TOTAL = 3   # Total single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_TOTAL = 4   # Total double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_AGG_TOTAL = 5   # Total single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_TOTAL = 6   # Total double bit aggregate (persistent) ECC errors

# Individual ECC locations
NVML_FI_DEV_ECC_SBE_VOL_L1 = 7      # L1 cache single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_L1 = 8      # L1 cache double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_VOL_L2 = 9      # L2 cache single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_L2 = 10     # L2 cache double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_VOL_DEV = 11    # Device memory single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_DEV = 12    # Device memory double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_VOL_REG = 13    # Register file single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_REG = 14    # Register file double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_VOL_TEX = 15    # Texture memory single bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_TEX = 16    # Texture memory double bit volatile ECC errors
NVML_FI_DEV_ECC_DBE_VOL_CBU = 17    # CBU double bit volatile ECC errors
NVML_FI_DEV_ECC_SBE_AGG_L1 = 18     # L1 cache single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_L1 = 19     # L1 cache double bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_SBE_AGG_L2 = 20     # L2 cache single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_L2 = 21     # L2 cache double bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_SBE_AGG_DEV = 22    # Device memory single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_DEV = 23    # Device memory double bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_SBE_AGG_REG = 24    # Register File single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_REG = 25    # Register File double bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_SBE_AGG_TEX = 26    # Texture memory single bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_TEX = 27    # Texture memory double bit aggregate (persistent) ECC errors
NVML_FI_DEV_ECC_DBE_AGG_CBU = 28    # CBU double bit aggregate ECC errors

# Page Retirement
NVML_FI_DEV_RETIRED_SBE = 29        # Number of retired pages because of single bit errors
NVML_FI_DEV_RETIRED_DBE = 30        # Number of retired pages because of double bit errors
NVML_FI_DEV_RETIRED_PENDING = 31    # If any pages are pending retirement. 1=yes. 0=no.

# NvLink Flit Error Counters
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L0 = 32     # NVLink flow control CRC  Error Counter for Lane 0
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L1 = 33     # NVLink flow control CRC  Error Counter for Lane 1
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L2 = 34     # NVLink flow control CRC  Error Counter for Lane 2
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L3 = 35     # NVLink flow control CRC  Error Counter for Lane 3
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L4 = 36     # NVLink flow control CRC  Error Counter for Lane 4
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_L5 = 37     # NVLink flow control CRC  Error Counter for Lane 5
NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_TOTAL = 38  # NVLink flow control CRC  Error Counter total for all Lanes

# NvLink CRC Data Error Counters
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L0 = 39     # NVLink data CRC Error Counter for Lane 0
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L1 = 40     # NVLink data CRC Error Counter for Lane 1
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L2 = 41     # NVLink data CRC Error Counter for Lane 2
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L3 = 42     # NVLink data CRC Error Counter for Lane 3
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L4 = 43     # NVLink data CRC Error Counter for Lane 4
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_L5 = 44     # NVLink data CRC Error Counter for Lane 5
NVML_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_TOTAL = 45  # NvLink data CRC Error Counter total for all Lanes

# NvLink Replay Error Counters
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L0 = 46       # NVLink Replay Error Counter for Lane 0
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L1 = 47       # NVLink Replay Error Counter for Lane 1
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L2 = 48       # NVLink Replay Error Counter for Lane 2
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L3 = 49       # NVLink Replay Error Counter for Lane 3
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L4 = 50       # NVLink Replay Error Counter for Lane 4
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L5 = 51       # NVLink Replay Error Counter for Lane 5
NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_TOTAL = 52    # NVLink Replay Error Counter total for all Lanes

# NvLink Recovery Error Counters
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L0 = 53     # NVLink Recovery Error Counter for Lane 0
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L1 = 54     # NVLink Recovery Error Counter for Lane 1
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L2 = 55     # NVLink Recovery Error Counter for Lane 2
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L3 = 56     # NVLink Recovery Error Counter for Lane 3
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L4 = 57     # NVLink Recovery Error Counter for Lane 4
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_L5 = 58     # NVLink Recovery Error Counter for Lane 5
NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_TOTAL = 59  # NVLink Recovery Error Counter total for all Lanes

# NvLink Bandwidth Counters
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L0 = 60     # NVLink Bandwidth Counter for Counter Set 0, Lane 0
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L1 = 61     # NVLink Bandwidth Counter for Counter Set 0, Lane 1
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L2 = 62     # NVLink Bandwidth Counter for Counter Set 0, Lane 2
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L3 = 63     # NVLink Bandwidth Counter for Counter Set 0, Lane 3
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L4 = 64     # NVLink Bandwidth Counter for Counter Set 0, Lane 4
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_L5 = 65     # NVLink Bandwidth Counter for Counter Set 0, Lane 5
NVML_FI_DEV_NVLINK_BANDWIDTH_C0_TOTAL = 66  # NVLink Bandwidth Counter Total for Counter Set 0, All Lanes

# NvLink Bandwidth Counters
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L0 = 67     # NVLink Bandwidth Counter for Counter Set 1, Lane 0
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L1 = 68     # NVLink Bandwidth Counter for Counter Set 1, Lane 1
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L2 = 69     # NVLink Bandwidth Counter for Counter Set 1, Lane 2
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L3 = 70     # NVLink Bandwidth Counter for Counter Set 1, Lane 3
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L4 = 71     # NVLink Bandwidth Counter for Counter Set 1, Lane 4
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_L5 = 72     # NVLink Bandwidth Counter for Counter Set 1, Lane 5
NVML_FI_DEV_NVLINK_BANDWIDTH_C1_TOTAL = 73  # NVLink Bandwidth Counter Total for Counter Set 1, All Lanes

# NVML Perf Policy Counters
NVML_FI_DEV_PERF_POLICY_POWER = 74              # Perf Policy Counter for Power Policy
NVML_FI_DEV_PERF_POLICY_THERMAL = 75            # Perf Policy Counter for Thermal Policy
NVML_FI_DEV_PERF_POLICY_SYNC_BOOST = 76         # Perf Policy Counter for Sync boost Policy
NVML_FI_DEV_PERF_POLICY_BOARD_LIMIT = 77        # Perf Policy Counter for Board Limit
NVML_FI_DEV_PERF_POLICY_LOW_UTILIZATION = 78    # Perf Policy Counter for Low GPU Utilization Policy
NVML_FI_DEV_PERF_POLICY_RELIABILITY = 79        # Perf Policy Counter for Reliability Policy
NVML_FI_DEV_PERF_POLICY_TOTAL_APP_CLOCKS = 80   # Perf Policy Counter for Total App Clock Policy
NVML_FI_DEV_PERF_POLICY_TOTAL_BASE_CLOCKS = 81  # Perf Policy Counter for Total Base Clocks Policy

# Memory temperatures
NVML_FI_DEV_MEMORY_TEMP = 82    # Memory temperature for the device

# Energy Counter
NVML_FI_DEV_TOTAL_ENERGY_CONSUMPTION = 83   # Total energy consumption for the GPU in mJ since the driver was last reloaded

# NVLink Speed
NVML_FI_DEV_NVLINK_SPEED_MBPS_L0 = 84       # NVLink Speed in MBps for Link 0
NVML_FI_DEV_NVLINK_SPEED_MBPS_L1 = 85       # NVLink Speed in MBps for Link 1
NVML_FI_DEV_NVLINK_SPEED_MBPS_L2 = 86       # NVLink Speed in MBps for Link 2
NVML_FI_DEV_NVLINK_SPEED_MBPS_L3 = 87       # NVLink Speed in MBps for Link 3
NVML_FI_DEV_NVLINK_SPEED_MBPS_L4 = 88       # NVLink Speed in MBps for Link 4
NVML_FI_DEV_NVLINK_SPEED_MBPS_L5 = 89       # NVLink Speed in MBps for Link 5
NVML_FI_DEV_NVLINK_SPEED_MBPS_COMMON = 90   # Common NVLink Speed in MBps for active links
NVML_FI_DEV_NVLINK_LINK_COUNT = 91          # Number of NVLinks present on the device
NVML_FI_DEV_RETIRED_PENDING_SBE = 92        # If any pages are pending retirement due to SBE. 1=yes. 0=no.
NVML_FI_DEV_RETIRED_PENDING_DBE = 93        # If any pages are pending retirement due to DBE. 1=yes. 0=no.
NVML_FI_MAX = 94                            # One greater than the largest field ID defined above


nvmlEventTypeSingleBitEccError = 0x0000000000000001     # Event about single bit ECC errors
nvmlEventTypeDoubleBitEccError = 0x0000000000000002     # Event about double bit ECC errors
nvmlEventTypePState = 0x0000000000000004                # Event about PState changes
nvmlEventTypeXidCriticalError = 0x0000000000000008      # Event that Xid critical error occurred
nvmlEventTypeClock = 0x0000000000000010                 # Event about clock changes. Kepler only
nvmlEventTypeNone = 0x0000000000000000                  # Mask with no events
nvmlEventTypeAll = (                                    # Mask of all events
    nvmlEventTypeNone |
    nvmlEventTypeSingleBitEccError |
    nvmlEventTypeDoubleBitEccError |
    nvmlEventTypePState |
    nvmlEventTypeClock |
    nvmlEventTypeXidCriticalError
)

nvmlClocksThrottleReasonGpuIdle = 0x0000000000000001                    # Nothing is running on the GPU and the clocks are dropping to Idle state
nvmlClocksThrottleReasonApplicationsClocksSetting = 0x0000000000000002  # GPU clocks are limited by current setting of applications clocks
nvmlClocksThrottleReasonSwPowerCap = 0x0000000000000004                 # SW Power Scaling algorithm is reducing the clocks below requested clocks
nvmlClocksThrottleReasonHwSlowdown = 0x0000000000000008                 # HW Slowdown (reducing the core clocks by a factor of 2 or more) is engaged
nvmlClocksThrottleReasonSyncBoost = 0x0000000000000010                  # Sync Boost
nvmlClocksThrottleReasonSwThermalSlowdown = 0x0000000000000020          # SW Thermal Slowdown
nvmlClocksThrottleReasonHwThermalSlowdown = 0x0000000000000040          # HW Thermal Slowdown (reducing the core clocks by a factor of 2 or more) is engaged
nvmlClocksThrottleReasonHwPowerBrakeSlowdown = 0x0000000000000080       # HW Power Brake Slowdown (reducing the core clocks by a factor of 2 or more) is engaged
nvmlClocksThrottleReasonDisplayClockSetting = 0x0000000000000100        # GPU clocks are limited by current setting of Display clocks
nvmlClocksThrottleReasonNone = 0x0000000000000000                       # Bit mask representing no clocks throttling
nvmlClocksThrottleReasonAll = (                                         # Bit mask representing all supported clocks throttling reasons
    nvmlClocksThrottleReasonNone |
    nvmlClocksThrottleReasonGpuIdle |
    nvmlClocksThrottleReasonApplicationsClocksSetting |
    nvmlClocksThrottleReasonSwPowerCap |
    nvmlClocksThrottleReasonHwSlowdown |
    nvmlClocksThrottleReasonSyncBoost |
    nvmlClocksThrottleReasonSwThermalSlowdown |
    nvmlClocksThrottleReasonHwThermalSlowdown |
    nvmlClocksThrottleReasonHwPowerBrakeSlowdown |
    nvmlClocksThrottleReasonDisplayClockSetting
)

# Buffer size guaranteed to be large enough for \ref nvmlVgpuTypeGetLicense
NVML_GRID_LICENSE_BUFFER_SIZE = 128
NVML_VGPU_NAME_BUFFER_SIZE = 64
NVML_GRID_LICENSE_FEATURE_MAX_COUNT = 3

# pGPU's virtualization capabilities bitfield
NVML_VGPU_PGPU_VIRTUALIZATION_CAP_MIGRATION = 0
NVML_VGPU_PGPU_VIRTUALIZATION_CAP_MIGRATION_NO = 0
NVML_VGPU_PGPU_VIRTUALIZATION_CAP_MIGRATION_YES = 1

# nvmlInitializationAndCleanup Initialization and Cleanup
NVML_INIT_FLAG_NO_GPUS = 1      # Don't fail nvmlInit() when no GPUs are found
NVML_INIT_FLAG_NO_ATTACH = 2    # Don't attach GPUs

# Buffer size guaranteed to be large enough for:
NVML_DEVICE_INFOROM_VERSION_BUFFER_SIZE = 16    # nvmlDeviceGetInforomVersion and nvmlDeviceGetInforomImageVersion
NVML_DEVICE_UUID_BUFFER_SIZE = 80               # nvmlDeviceGetUUID
NVML_DEVICE_PART_NUMBER_BUFFER_SIZE = 80        # nvmlDeviceGetBoardPartNumber
NVML_SYSTEM_DRIVER_VERSION_BUFFER_SIZE = 80     # nvmlSystemGetDriverVersion
NVML_SYSTEM_NVML_VERSION_BUFFER_SIZE = 80       # nvmlSystemGetNVMLVersion
NVML_DEVICE_NAME_BUFFER_SIZE = 64               # nvmlDeviceGetName
NVML_DEVICE_SERIAL_BUFFER_SIZE = 30             # nvmlDeviceGetSerial
NVML_DEVICE_VBIOS_VERSION_BUFFER_SIZE = 32      # nvmlDeviceGetVbiosVersion
