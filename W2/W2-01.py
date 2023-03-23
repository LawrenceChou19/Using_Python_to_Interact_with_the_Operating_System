file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()


#improve
with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())#fix blank line issue


with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())

file = open("spider.txt")
lines = file.readlines()
file.close()
#test even close the file the data still keep in lines value
lines.sort()
print(lines)

with open("novel.txt","w") as file:
    file.write("It was a dark and stormy night")


