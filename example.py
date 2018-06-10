from nvml import NVML


def main():
    with NVML() as nvml:
        device_count = nvml.deviceGetCount()
        print(f"Found number of devices: {device_count}")
        for gpu in nvml.getAllGPUs():
            print(gpu)
            # print(gpu.getUtilizationRates())
            print(gpu.getEncoderStats())


if __name__ == "__main__":
    main()
