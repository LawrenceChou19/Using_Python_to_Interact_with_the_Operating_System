#[time_to_automate < (time_to_perform * amount_of_times_done)]

import shutil
du = shutil.disk_usage("/")
print(du)


# wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
# sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
# sudo apt-get update
# sudo apt-get install atom

import psutil
cu = psutil.cpu_percent(0.1)
print(cu)

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