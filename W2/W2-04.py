# Prerequisites
# cd data
# ls
# cat employees.csv
# cd ~/scripts
# nano generate_report.py

#!/usr/bin/env python3
# Convert employee data to dictionary

import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list
employee_list = read_employees('.\employee.csv') #need to modify the csv file location
print(employee_list)

# chmod +x generate_report.py
# ./generate_report.py

# Process employee data
# nano generate_report.py
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)
print(dictionary)

# ./generate_report.py

# Generate a report
# nano generate_report.py
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
write_report(dictionary, ".\\report.txt") #need to modify the report location

# ./generate_report.py
# cd ~/data
# ls
# cat report.txt