#!/usr/bin/env python3
#-*- coding utf-8 -*-

# import subprocess
# print(subprocess.run)
# subprocess.run(["date"])
# subprocess.run(["sleep","2"])
# result= subprocess.run(["ls","this_file_does_not_exist"])
# print(result.returncode)

# print("===============================================")
# result = subprocess.run(["host","8.8.8.8"], capture_output=True)#, shell=True
# print(result.returncode)

# print(result.stdout)
# print(result.stdout.decode().split())
# result = subprocess.run(["rm","does_not_exist"],capture_output=True)
# print(result.returncode)
# print(result.stdout)
# print(result.stderr)

print("===============================================")
import os
import subprocess
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/",my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)
subprocess.run(['start', 'current_roster.xlsx'], shell=True)