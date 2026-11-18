"""
def display():
    print("welcome to function")
display()
display()
display()

                   
def sum(a, b):                             # defining a function
    print("Sum of two values=", (a+b))
sum(20,30)                                 # calling function

def sum(a,b):
    c=a+b
    return c
x=sum(1,2)
print("Sum of two numbers is:",x)

def m1():
    print("This function is returning nothing")
m1()
x=m1()
print(x)

def m1(a, b):
   c = a+b
   d = a-b
   return c, d
x, y = m1(10, 5)
print("sum of a and b: ", x)
print("subtraction of a and b: ", y)

def m1():
    print("first function information")
def m2():
    print("second function information")
    m1()
m2()

#All functions in Python are first-class functions:pass around and manipulate other kinds of objects

def add():                                          #Assigning a function to a variable
    print("We assigned function to variable")
sum=add
sum()

def add(a,b):             
    return a+b
abcd=add
print(abcd(12,34))

def process(x,y,func):     #function can be passed to another function as an argument
    print("Sum is ",func(x,y))
process(12,34,abcd)

def display(x):
    print("This is display function")
def message():
    print("This is message function")
display(message())         #First inner function is called then outer function is called

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

def sum(a, b):
    c = a + b                  # a and b are formal arguments
    print(c)
x = 10
y = 15
sum(x, y)                      # x and y are actual arguments

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

s = lambda a: a*a
x=s(4)
print(x)

add = lambda a,b: a+b
x=add(4,5)
print(x)

items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)

without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)

from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)

def m():
    yield 'Mahesh'
    yield 'Suresh'
g = m()
print(g)
print(type(g))
for y in g:
    print(y)

def m(x, y):
    while x<=y:
        yield x
        x+=1
g = m(5, 10)
for y in g:
    print(y)

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
"""

                











