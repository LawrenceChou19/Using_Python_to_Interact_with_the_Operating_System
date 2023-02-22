import re
result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result)
print(result.groups())

print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2],result[1]))

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
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$",name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

print('=============================================================')

print(re.search(r"[a-zA-Z]{5}","a ghost"))
print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared"))
print(re.findall(r"\w{5,10}","I really like strawberries"))
print(re.findall(r"\w{5,}","I really like strawberries"))
print(re.search(r"s\w{,20}","I really like strawberries"))

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

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

import re
def transform_record(record):
  # new_search = re.findall(r"\d+-\d+-*\d+",record)
  # new_record = re.sub(r"\d+-\d+-*\d+","+1-"+new_search[0],record) # bad solution

  new_record = re.sub(r"(\d+-\d+-*\d+)",r"+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

import re
def multi_vowel_words(text):
  pattern = r"\w+[aeiou]{3}\w+"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

import re
def transform_comments(line_of_code):
  result = re.sub(r"#+","//",line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

import re
def convert_phone_number(phone):
    # new_search = re.findall(r"\b(\d{3})-(\d{3})-(\d{4})\b",phone)
    # print(new_search)
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b",r"(\1) \2-\3", phone)

    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300