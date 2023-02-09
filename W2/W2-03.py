import csv
f= open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name,phone,role = row
    print("Name:{},Phone:{},Role:{}".format(name,phone,role))
f.close()

hosts =[["workstation.local","192.168.25.46"],["webserver.cloud","10.25.5.6"]]
with open('hosts.csv','w') as host_csv:#generate a hosts csv file
    writer = csv.writer(host_csv)
    writer.writerows(hosts) #writerow = one row, writerows = all of the them


with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"],row["users"]))

users = [{"name":"Sol Mansi","username":"solm","department":"IT infrastructure"},{"name":"Lio Nelson","username":"lion","department":"User Experience Research"},{"name":"Charlie Grey","username":"greyc","department":"Development"},]
keys = ["name","username","department"]
with open('by_department.csv','w') as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()#creat first line of header(keys)
    writer.writerows(users) #write all of values