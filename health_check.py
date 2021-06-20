import shutil
import psutil

def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free
    total = du.total
    check = free/total*100
    return check>10

def cpu_percent():
    
    usage = psutil.cpu_percent(1)
    return usage<50


if not disk_usage("/") or not cpu_percent():
    print("Error cool down or remove some space")
else:
    print("Every thing is fine") 

