#pip install psutil
import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("CPU Usage:", cpu, "%")
print("Memory Usage:", memory, "%")
print("Disk Usage:", disk, "%")

if cpu > CPU_THRESHOLD:
    print("ALERT: CPU usage is high!")

if memory > MEMORY_THRESHOLD:
    print("ALERT: Memory usage is high!")

if disk > DISK_THRESHOLD:
    print("ALERT: Disk usage is high!")
