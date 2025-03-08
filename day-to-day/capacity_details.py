import shutil
import psutil

total , used , free = shutil.disk_usage("/")

print("Disk Usage:")
print(f"Total disk capacity: {(total // 2**30)}GB")
print(f"Total disk used: {( used // 2**30)}GB")
print(f"Total free disk: {(free // 2**30)}GB")

cpu_percent = psutil.cpu_percent(interval=2)
print(f"\nCPU usage: {cpu_percent}")

ram = psutil.virtual_memory()
print(f"\nRam Usage:")
print(f"   Total ram capacity: {(ram.total // 2**30)}GB")
print(f"   Total ram Usage: {(ram.used // 2**30)}GB")
print(f"   Total free ram: {(ram.available // 2**30)}GB")
print(f"   Total used ram: {ram.percent}%")

