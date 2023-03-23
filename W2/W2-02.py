
import os
# os.remove("novel.txt")
# os.rename("first_darft.txt","finished_masterpiece.txt")
print(os.path.exists("finished_masterpiece.txt"))
os.path.exists("userlist.txt")

print('================================================================')
print(os.path.getsize("spider.txt"))
print(os.path.getmtime("spider.txt"))
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
print(datetime.datetime.fromtimestamp(timestamp))

file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
print("File not found")

print(os.path.abspath("spider.txt"))
print('================================================================')

print(os.getcwd())
try:
    os.removedirs("new dir")
except OSError as e:
    print('Delete Problem: ', e)

os.mkdir("new dir")#create
os.chdir("new dir")#move to folder path
print(os.getcwd())
# os.rmdir("new dir")#delete
# os.removedirs("new dir")

print(os.getcwd())
# os.rmdir("newer_dir")#delete
# os.mkdir("newer_dir")#create


print('================================================================')
os.chdir("new dir")#move to folder path
os.listdir("website")
dir = "website" #dir path
for name in os.listdir(dir): #load path to name
    # print('from listdir to name value is',name)
    fullname = os.path.join(dir,name)
    # print(fullname)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


