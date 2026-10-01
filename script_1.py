#информация об операционной системе, процессоре
import platform
#имя компьютера
import socket
#информция о количестве логических процессоров
import os
# информация о диске
import shutil
# json
import json

system=platform.system()
if system == "Darwin":
    system="MacOs"

vertion=platform.release()
architecture=platform.machine()
computer_name=socket.gethostname()
processor=platform.processor()
cpu_count = os.cpu_count()
if system=="Windows":
    disk=shutil.disk_usage("C:\\")
else:
    disk=shutil.disk_usage("/")
disk_total=round(disk.total/1024**3,2)
disk_free=round(disk.free/1024**3,2)

info={
    "os": system,
    "os_version": vertion,
    "architecture": architecture,
    "computer_name": computer_name,
    "processor": processor,
    "cpu_count": cpu_count,
    "disk_total_gb": disk_total,
    "disk_free_gb": disk_free
}
print(info)
with open("system_info.json","w",encoding="utf-8") as file:
    json.dump(info,file,indent=4,ensure_ascii=False)





