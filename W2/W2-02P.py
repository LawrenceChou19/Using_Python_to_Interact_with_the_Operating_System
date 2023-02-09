
# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open("program.py",'w') as filesize:
#     filesize = filesize.write(comments)
#   return(filesize)

# print(create_python_script("program.py"))


import time
import os
start = time.time()
def new_directory(directory, filename):
# Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename,"w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
end = time.time()
print("執行時間：%f 秒" % (end - start))

import time
import os
start = time.time()
def new_directory(directory, filename):
# Before creating a new directory, check to see if it already exists
    if os.path.exists(directory) == False:
        os.makedirs(directory)
    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename,"w") as file:
        pass
    # Return the list of files in the new directory
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

end = time.time()
print("執行時間：%f 秒" % (end - start))

# import os
# import datetime

# def file_date(filename):
#     # Create the file in the current directory
#     os.mkdir(filename)
#     timestamp = os.path.getmtime(filename)
#     # Convert the timestamp into a readable format, then into a string
#     date = datetime.date.fromtimestamp(timestamp)
#     # Return just the date portion 
#     # Hint: how many characters are in “yyyy-mm-dd”? 
#     return ("{}".format(date))

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd

# import os
# def parent_directory():
#   # Create a relative path to the parent 
#   # of the current working directory 
#   relative_parent = os.path.join(os.getcwd(),os.pardir)# "ls" + ".." + "ls" in console

#   # Return the absolute path of the parent directory
#   return os.path.abspath(relative_parent)

# print(parent_directory())