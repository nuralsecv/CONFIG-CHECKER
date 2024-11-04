import psutil
import GPUtil
import platform
from datetime import datetime

# System Information
print("System Information")
print("="*40)
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print("="*40)

# Memory (RAM) Information
print("Memory Information")
print("="*40)
svmem = psutil.virtual_memory()
print(f"Total: {svmem.total / (1024 ** 3):.2f} GB")
print(f"Available: {svmem.available / (1024 ** 3):.2f} GB")
print(f"Used: {svmem.used / (1024 ** 3):.2f} GB")
print(f"Percentage: {svmem.percent}%")
print("="*40)

# GPU Information
print("GPU Information")
print("="*40)
gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"ID: {gpu.id}")
    print(f"Name: {gpu.name}")
    print(f"Total Memory: {gpu.memoryTotal}MB")
    print(f"Free Memory: {gpu.memoryFree}MB")
    print(f"Used Memory: {gpu.memoryUsed}MB")
    print(f"Load: {gpu.load * 100}%")
    print(f"Temperature: {gpu.temperature} °C")
    print("="*40)
