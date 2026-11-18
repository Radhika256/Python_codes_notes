"""
import os, sys
fname=input("Enter File Name:")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does noe exist:",fname)
    sys.exit(0)
print("The content of file is:")
data=f.read()
print(data)

import csv
with open("emp.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["EMP NO","EMP NAME","EMP SAL","EMP ADDR"])
    n=int(input("Enter the Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Total Employees data written to csv file successfully")

import csv
with open("emp.csv","r",newline='')as f:
    r = csv.reader(f)
    print("EMP NO\tEMP NAME\tEMP SAL\tEMP ADDR")
    for row in r:
        print("\t".join(row))
print("Total Employees data read from csv file successfully")

n=int(input("Enter no. of password:"))
for i in range(n):
    p=input("Enter Password:")
    if len(p)>=8:
        count=0
        for a in p:
            if a.upper():
                count+=1
            elif a.lower():
                count+=1
            elif a.isdigit():
                count+=1
            elif a in ["!","@","#","$","%","^","&","*"]:
                count+=1
            elif a.isspace():
                count+=0
            else:
                count+=0
        print() 
"""
