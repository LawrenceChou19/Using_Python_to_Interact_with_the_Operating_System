import re
result = re.search(r"aza","plaza")
print('re.search(r"aza","plaza")',result)

result = re.search(r"aza","bazaar")
print('re.search(r"aza","bazaar")',result)
result = re.search(r"aza","maze")
print('re.search(r"aza","maze")',result)
result = re.search(r"p.ng","penguin")
print('re.search(r"p.ng","penguin")',result)
result = re.search(r"p.ng","clapping")
print('re.search(r"p.ng","clapping")',result)
result = re.search(r"p.ng","sponge")
print('re.search(r"p.ng","sponge")',result)
result = re.search(r"p.ng","Pangaea",re.IGNORECASE)
print('re.search(r"p.ng","Pangaea",re.IGNORECASE)',result)

print("======================================================")
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None
print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


print("======================================================")


print(re.search(r"[Pp]ython","Python"))
print(re.search(r"[a-z]way","The end of the highway"))
print(re.search(r"[a-z]way","What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]","cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]","cloud9"))
print("======================================================")
import re
def check_punctuation (text):
  result = re.search(r"[\.!\?]+$", text) #One or more of the punctuations (., !, or ?) after the second run of small letters, and then the string ends.
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print("======================================================")

print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces."))
print(re.search(r"cat|dog","I like cats."))
print(re.search(r"cat|dog","I like dogs."))
print(re.search(r"cat|dog","I like dogs and cats."))
print(re.findall(r"cat|dog","I like dogs and cats."))

print("======================================================")

print(re.search(r"Py.*n","Pygmalion"))
print(re.search(r"Py.*n","Python_Programming"))
print(re.search(r"Py[a-z]*n","Python_Programming"))

print(re.search(r"o+l+","goldfish"))
print(re.search(r"o+l+","woolly"))
print(re.search(r"o+l+","boil"))

import re
def repeating_letter_a(text):
  result = re.search(r"^[a-bA-Z]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

print("======================================================")

print(re.search(r"p?each","To each their own"))
#<re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each","I like peaches"))
#<re.Match object; span=(7, 12), match='peach'>


print(re.search(r".com","welcome"))
#<re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com","welcome"))
#None
print(re.search(r"\.com","mydomain.com"))
#<re.Match object; span=(8, 12), match='.com'>
print(re.search(r"\w*","This is an example"))
#<re.Match object; span=(0, 4), match='This'>
print(re.search(r"\w*","And_this_is_another")) 
#\w matches letters <re.Match object; span=(0, 19), match='And_this_is_another'>
print(re.search(r"\d","And_this_is_another123")) 
#\d for matching digits <re.Match object; span=(19, 20), match='1'>
print(re.search(r"\s*","And this is another")) 
#\s for matching whitespace characters like space <re.Match object; span=(0, 0), match=''>
print(re.search(r"\b","And+this_is_another"))
#<re.Match object; span=(0, 0), match=''>

import re
def check_character_groups(text):
  result = re.search(r"\w+\s", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

print("======================================================")

print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a$","Azerbaijan"))
print(re.search(r"A.*a$","Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable_name"))
#<re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
print(re.search(pattern,"this is a valid variable"))
#None
print(re.search(pattern,"my_variable1"))
#<re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern,"2my_variable1"))
#None

import re
def check_sentence(text):
  result = re.search(r"^[A-Z]+[a-z\s]+[\.\?!]$", text)# ^[A-Z]+ = uppercase letter , [a-z\s]+ = at least some lowercase letter or space, [\.\?!]$ = a period, question mark, or exclamation point 
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

print("======================================================")


content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)


import re
p = re.compile('[a-z]+')
print(p)
print(p.match('::: message'))
m = p.search('::: message'); print(m)
print(m.group())
print(m.span())
p = re.compile(r'\d+')
print(p.search('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))