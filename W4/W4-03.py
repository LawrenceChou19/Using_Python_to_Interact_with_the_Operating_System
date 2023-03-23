#!/usr/bin/env python
#try W4-03.py syslog
import re 
import sys
print(sys.argv[0])
logfile=sys.argv[1]
logfile=sys.argv[1]
with open(logfile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		print(result[1])

import re
def show_time_of_pid(line):

  pattern = r"(\w+ \d \d+\:\d+\:\d+) \w.+ [\w=_]+\[([0-9]+)\]"
  #(\w+ \d \d+\:\d+\:\d+)= Jul 6 14:01:23, 
  # \w.+ = computer.name  
  # [\w=_]+\[([0-9]+)\] = CRON[29440] or jam_tag=psim[29187]
  result = re.search(pattern, line)
#   print(result.groups())
  return '{} pid:{}'.format(result[1],result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

import re
def show_time_of_pid(line):

  pattern = r"(\w+ \d \d+\:\d+\:\d+) \w.+ [\w=_]+\[([0-9]+)\]:(\w*)"
  #(\w+ \d \d+\:\d+\:\d+)= Jul 6 14:01:23, 
  # \w.+ = computer.name  
  # [\w=_]+\[([0-9]+)\] = CRON[29440] or jam_tag=psim[29187]
  result = re.search(pattern, line)
#   print(result.groups())
#   return '{} pid:{}'.format(result[1],result[2])
  return result

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


print("========================================================================")

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name,0)+1
print(usernames)
usernames[name] = usernames.get(name,0)+1
print(usernames)

#!/usr/bin/env python3

import re 
import sys

logfile=sys.argv[1]
with open(logfile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		if result is None:
			continue
		name = result[1]
		usernames[name] = usernames.get(name, 0)+1
print(usernames)