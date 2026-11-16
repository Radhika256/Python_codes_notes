"""
def add(a,b):             #function can be assigned to variable
    return a+b
abcd=add
print(abcd(12,34))

def process(x,y,func):     #function can be passed to another function as an argument
    print("Sum is ",func(x,y))
process(12,34,abcd)

def outer():                #function inside function
    print("Outer Function")
    def inner():
        print("Inner Function")
    inner()
outer()

def outer():                 #function can return another function
    print("Outer Function")
    def inner():
        print("Inner Function")
    return inner
func1=outer()     #print("Outer Function")
func1()           #print("Inner Function")

def createfunction():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    return add,sub
func1,func2=createfunction()
print(func1(12,34))
print(func2(12,34))

def details(name,age):
    print("Name is ",name)
    print("Age is ",age)
details("Amit",12)                     #Positional Arguments
details(age=12,name="Amit")            #Keyword Arguments(order doesn't matter)
details(name="Suraj",age=12)

def details(name,age=12):
    print("Name is ",name)
    print("Age is ",age)
details(name="Amit")                   #default arguments
details(name="Amit",age=15)

def add(a,*b):                         #variable length arguments
    print(type(a))
    print(type(b))
    sum=0
    for i in b:
        sum+=i
    return sum+a

print(add(12,34,45,56,78))           #225
print(add(12,34,45,56,78,56,89,99))  #469
print(add(12,))   #12
print(add(12))    #12
print(add())      #error

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(id=1,name="Jack",qualification="MBA")

def m1(**x):
    for k,v in x.items():
        print(k,"=",v)
m1(a=10,b=20,c=30)
m1(id=100,name="Subbalaxmi")

def m():
    a=11
    print(a)
m()

def m():
    a=11
    print(a)
def n():    
    print(a)               #name error
m()
n()

a=11
b=12
def m():
    print("a from function m():",a)
    print("b from function m():",b)
def n():
    print("a from function n():",a)
    print("b from function n():",b)
m()
n()

a=1
def m1():
    a=2
    print("a from function m1():",a)
def m2():
    print("a from function m2():",a)
m1()
m2()

a=1
def m1():
    global a
    a=2
    print("a from function m1():",a)
def m2():
    print("a from function m2():",a)
m1()
m2()

a=1
def m():
    a=2
    print(a)
    print(globals()["a"])
m()

def printdata(x):
    if x==5:
        return
    else:
        print(x)
        printdata(x+1)
printdata(1)

def printdata(x):
    if x==5:
        return
    else:
        printdata(x+1)
        print(x)
printdata(1)

def printdata(x):
    if x==5:
        print("complete")
    else:
        print(x)
        printdata(x+1)
printdata(1)

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
print(fact(5))

def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
print(power(2,4))

while True:
    num=int(input("Enter:"))
    print(num)
    if not num > 0:
        break

def m(x,y):
    while x<=y:
        yield x
        x+=1
g=m(5,10)
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))       #StopIteration

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

                











