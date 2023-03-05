#Below we have some code that makes a list of specific letters found in any string. 
#If you run it, you can see what it does.
import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))