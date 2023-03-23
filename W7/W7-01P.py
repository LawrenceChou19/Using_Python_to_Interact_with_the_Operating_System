# grep ticky syslog.log
# grep "ERROR" syslog.log
# grep "ERROR Tried to add information to closed ticket" syslog.log
# python3

import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)
#<_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)
#<_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
#[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

with open("syslog.log", 'r') as f:
  print(f.readlines())
#test
