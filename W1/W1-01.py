import re 
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Persforming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex,log)
print(result[1])

#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")

import requests
response = requests.get("http://www.google.com")
print(len(response.text))



import pandas
visitors = [1235,6424,9345,8464,2345]
errors = [23,45,33,45,76]
df = pandas.DataFrame({"visitors":visitors,"error":errors}, index=["Mon","Tues","Wed","Thu","Fri"])
print(df)
print(df["error"].mean())
