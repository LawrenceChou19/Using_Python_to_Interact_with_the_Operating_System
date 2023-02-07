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

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)