import re
result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result)
#<re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(result.groups())
#('Lovelace', 'Ada')
print(result[0])
#Lovelace, Ada
print(result[1])
#Lovelace
print(result[2])
#Ada
#test
print("{} {}".format(result[2],result[1]))
#Ada Lovelace

def rearrange_name(name):
    result = re.search(r"(\w*), (\w*$)",name)
    if result is None:
        return name
    return "Is {} {}".format(result[2],result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w.*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$",name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

name = rearrange_name("Hopper, Grace M.")
print(name)

print('=============================================================')

print(re.search(r"[a-zA-Z]{5}","a ghost"))
#<re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))
# <re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))
# ['scary', 'ghost', 'appea']
print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared"))
#['scary', 'ghost']
print(re.findall(r"\w{5,10}","I really like strawberries"))
# ['really', 'strawberri']
print(re.findall(r"\w{5,}","I really like strawberries"))
# ['really', 'strawberries']
print(re.search(r"s\w{,20}","I really like strawberries"))
# <re.Match object; span=(14, 26), match='strawberries'>

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


print('=============================================================')

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex,"A completely different string that also has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")
# print(result[1])

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w{5,7})"
    result = re.search(regex, log_line)
    # print( result)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

print('=============================================================')

print(re.split(r"[.?!]","One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])","One sentence. Another one? And the last one!"))
print(re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","Received an eamil for og_nuts95@my.example.com"))
print(re.sub(r"([\w .-]*), ([\w .-]*)$",r"\2 \1","Lovelace, Ada"))
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))



