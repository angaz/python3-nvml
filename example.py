from nvml import NVML


def main():
    with NVML() as nvml:
        device_count = nvml.deviceGetCount()
        print(f"Found number of devices: {device_count}")
        for gpu in nvml.getAllGPUs():
            print(gpu)
            print(f"Brand: {gpu.brand.brandName}")
            print(f"Serial: {gpu.serial}")
            print(f"UUID: {gpu.uuid}")
            print(f"PCI Info: {gpu.pciInfo}")
            print(f"Compute Processes: {gpu.getComputeRunningProcesses()}")
            print(f"Process Utilization: {gpu.getProcessUtilization()}")
            print(f"Encoder Sessions: {gpu.getEncoderSessions()}")

            utilization = gpu.getUtilizationRates()
            print(f"Utilization GPU: {utilization.gpu}% Memory: {utilization.memory}%")

            sessionCount, aveFPS, aveLatency = gpu.getEncoderStats()
            print(f"Encoder Stats: Session Count: {sessionCount}, Average FPS: {aveFPS}, Average letency: {aveLatency}")


if __name__ == "__main__":
    main()
