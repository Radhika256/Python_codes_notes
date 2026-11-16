"""
print("Hello World")

age=110
print(age)

a,b,c=1,2,3
print(a,b,c)

a,b,c=1,2
print(a,b,c)             #value error

a=b=c=1
print(a,b,c)

a=10
a=20
print(a)

a=10
b="Radhika"
print("Type of a:",type(a))     #To check the type of variable
print("Type of b:",type(b))

a=10
b=2e3
c=2+3j
d=complex(2,3)
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a=True
b=False
print(a)
print(b)
print(a+b)
print(a+a)

a=None
print(a)
print(type(a))

name="Radhika"
print(name)
print(type(name))

x=[1,2,3,4,5]
y=bytes(x)
print(y)              #b'\x01\x02\x03\x04\x05' It give value in bytes format
print(type(y))

x=[1,2,3,4,5]
y=bytes(x)
print(y[0])
print(y[10])          #IndexError: index out of range

a=range(10)
print(a)              #only print till 9

a="5"
b=int(a)
print(type(a))
print(type(b))

a=20
b=10
print(a+b)            #Arithmetic operations
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a>b)            #relational operations
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b and a<b)     #logical operations
print(a>b or a<b)
print(not a>b)
print(-a)              #uniary minus operation

a=10
b=20
a+=10           #Assignment operations
b-=10
print(a)
print(b)

a="I am Radhika"
b="am"
print(b in a)       #membership operations
print(b not in a)

a=10
b=20
print(id(a))
print(id(b))
print(a is b)        #identity operations
print(a is not b)

a=input("Enter a number:")
print(a)
print(type(a))

a=int(input("Enter a number:"))
print(a)
print(type(a))

a=eval('10+20')
print(a)

from sys import argv
print("Number of arguments:", len(argv))
print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])

a='''I am Radhika
hello
I am learning python'''
print(a)

s1="I am 'Radhika'"
print(s1)

s1=""
print(s1)

s1="I am learning python"
print(s1[0])
print(s1[0:5])

name="Radhika"
name[0]="r"          #TypeError: 'str' object does not support item assignment
print(name)

a="python "
b="programming"
c=3
print(a+b)
print(a*c)

a="python"
print(a[-4:-1])

a="python"
print(a.center(10),"hello")
print(len(a.center(10)))

s1 = "abcd"
s2 = "abcdefg"
print(s1 == s2)
if(s1 == s2):
    print("Both are same")
else:
    print("not same")

course="Python programming language"
print(course.find("p"))
print(course.find("a", 1, 20))

s="Python programming language"
print(s.index("Python"))

s="Python programming language, Python is easy"
print(s.count("Python"))
print(s.count("Hello"))

s1="Java programming language"
s2=s1.replace("Java", "Python")
print(s1)
print(s2)
print(id(s1))
print(id(s2))

message="Python programming language"
n=message.split()
print("Before splitting: ",message)
print("After splitting: ",n)
print(type(n))
for x in n:
    print(x)

message="Python programming language,Python is easy"
n=message.split(",")
print(n)

profile = ['Roshan', 'Actor', 'India']
candidate = '-'.join(profile)
print(profile)
print(candidate)

name='Rakesh'
salary=100
age=16
print("{} 's salary is {} and his age is {}".format(name, salary, age))
print("{0} 's salary is {1} and his age is {2}".format(name, salary, age))
print("{x} 's salary is {y} and his age is{z}".format(z=age,y=salary,x=name))

name = 'John'
message = f'Hi {name}'
print(message)

a=" Python is a programming language  "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
"""
