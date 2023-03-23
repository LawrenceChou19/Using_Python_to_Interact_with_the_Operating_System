# def to_seconds(hours, minutes, seconds):
#     return hours*3600+minutes*60+seconds
# print("Welcome to this time ocnverter")

# cont = "y"
# while (cont.lower()=='y'):
#     hours = int(input("Enter the number of hours: "))
#     minutes = int(input("Enter the number of minutes: "))
#     seconds = int(input("Enter the number of hours: "))

#     print("That's {} seconds".format(to_seconds(hours,minutes, seconds)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")
# print("Good bye!")

print("===============================================")

data= input("This will come from STDIN: ")
print("Now we write it to STDOUT: " +data)
# print("Now we generate an error to STDERR: " + data +1)

print("===============================================")
#!/usr/bin/env python3
import os 
print("HOME: " + os.environ.get("HOME",""))
print("SHELL: " + os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT",""))


print("===============================================")
#!/usr/bin/env python3
#-*- coding utf-8 -*-

import subprocess

print(subprocess.run)
subprocess.run(["dir"],shell =True)
subprocess.run(["date"], shell=True)
subprocess.run(["sleep","2"], shell=True)
result = subprocess.run(["host","8.8.8.8"], capture_output=True)#, shell=True
print(result.stdout)
print(result.stdout.decode().split())
result = subprocess.run(["rm","does_not_exist"],capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)


print("===============================================")
import os
import subprocess
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/",my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env,shell=True)
subprocess.run(['start', 'current_roster.xlsx'], shell=True)