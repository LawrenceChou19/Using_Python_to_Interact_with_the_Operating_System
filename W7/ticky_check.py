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
import operator
sorted(fruit.items(), key=operator.itemgetter(0))
sorted(fruit.items(), key=operator.itemgetter(1))
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)


# sudo chmod +x csv_to_html.py
# sudo chmod  o+w /var/www/html
# ./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html
# ls /var/www/html

Errormsg ={}
userstat ={}
Erropattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)' #ticky: ERROR The ticket was modified while updating (breee)
INFOpattern = r'ticky: INFO.* \((.+)\)' #ticky: INFO Created ticket [#4217] (mdouglas)

import re
import csv
import operator
def exportlogfile(logfile):
  with open(logfile,'r') as file:
    for log in file.readlines():
      # error_patterns = ["ERROR"]
      if re.search(Erropattern,log):
        export= re.search(Erropattern,log)
        Errormsg.setdefault(export.group(1),0)
        Errormsg[export.group(1)]+=1
        userstat.setdefault(export.group(2),[0,0])[1]+=1
      if re.search(INFOpattern,log):
        export= re.search(INFOpattern,log)
        userstat.setdefault(export.group(1),[0,0])[0]+=1
  # errorsorted = sorted(Errormsg.items(),key = lambda x: x[1],reverse=True) 
  errorsorted = sorted(Errormsg.items(),key = lambda x: x[1],reverse=True)     
  userstatsorted = sorted(userstat.items())            
  print(errorsorted)
  print(userstatsorted)
  with open('error_message.csv','w') as output:
    writer = csv.writer(output)
    writer.writerow(['Error','Count'])      
    for item in errorsorted:
      onerow = [item[0],item[1]]
      writer.writerow(onerow)
  with open('user_statistics.csv','w') as output:
    writer = csv.writer(output)
    writer.writerow(['Username','INFO','ERROR'])
    for item in userstatsorted:
      onerow = [item[0],item[1][0],item[1][1]]
      writer.writerow(onerow)
    
print(exportlogfile("syslog.log"))

# chmod +x ticky_check.py
# ./ticky_check.py

    
# t = """
# dogs_3351.txt:34.13559322033898
# cats_1875.txt:23.25581395348837
# cats_2231.txt:22.087912087912088
# elephants_3535.txt:37.092592592592595
# fish_1407.txt:24.132530120481928
# fish_2078.txt:23.470588235294116
# fish_2041.txt:23.564705882352943
# fish_666.txt:23.17241379310345
# fish_840.txt:21.77173913043478
# """

# import re

# d = {}
# for p, q in re.findall(r'^(.+?)_.+?:(.+)', t, re.M):
#     # print('q=',q)
#     d.setdefault(p, []).append(q)

# print(d)



#!/usr/bin/env python3

# import re
# import operator
# import os
# import csv

# error_msg = {}
# user_stat = {}

# error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
# info_pattern = r'ticky: INFO.* \((.+)\)'

# with open('syslog.log','r') as logs:
#   for line in logs.readlines():
#     if re.search(error_pattern,line):
#       extracts = re.search(error_pattern, line)
#       error_msg.setdefault(extracts.group(1),0)
#       error_msg[extracts.group(1)]+=1
#       user_stat.setdefault(extracts.group(2),[0,0])[1]+=1
#     if re.search(info_pattern,line):
#       extracts = re.search(info_pattern, line)
#       user_stat.setdefault(extracts.group(1),[0,0])[0]+=1

# error_sorted = sorted(error_msg.items(), key = operator.itemgetter(1), reverse = True)
# user_sorted = sorted(user_stat.items())
# print(error_sorted)
# print(user_sorted)

# with open('error_message.csv','w') as output:
#   writer = csv.writer(output)
#   writer.writerow(['Error','Count'])
#   writer.writerows(error_sorted)

# with open('user_statistics.csv','w') as output:
#   writer = csv.writer(output)
#   writer.writerow(['Username','INFO','ERROR'])
#   for item in user_sorted:
#       onerow = [item[0],item[1][0],item[1][1]]
#       writer.writerow(onerow)