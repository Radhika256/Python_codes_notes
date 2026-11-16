"""
l1 = []
print(l1)
print(type(l1))

names = ["Mohan", "Prasad", "Ramesh", "Mohan", 10, 20, True, None]
print(names)

r=range(0, 10)
l=list(r)
print(l)

l = [1, 2, 3, 4, 5]
print(l)
print("Before modifying l[0] : ",l[0])
l[0]=20
print("After modifying l[0] : ",l[0])
print(l)

names = ["Prabhas", "Prashanth", "Prakash"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(type(names))
print(type(names[0]))
print(type(names[1]))
print(type(names[2]))

names = ["Prabhas", "Prashanth", "Prakash"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[10])         #Index error

n = [1, 2, 3, 4, 5, 6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])

a = [100, 200, 300, 400]
for x in a:
    print(x)

a = [100, 200, 300, 400]
x = 0
while x<len(a):
    print(a[x])
    x = x+1

n = [1, 2, 3, 4, 5]
print(len(n))

n = [1, 2, 3, 4, 5, 5, 5, 3]
print(n.count(5))
print(n.count(3))
print(n.count(2))

l=[]                         #empty list
l.append("Ramesh")
l.append("Suresh")
l.append("Naresh")
print(l)

n=[10, 20, 30, 40, 50]
n.insert(0, 76)
print(n)

l=[10, 20, 30, 40]
print(l)                   # [10, 20, 30, 40]
l.insert(1, 111)
print(l)                   # [10, 111, 20, 30, 40]
l.insert(-1, 222)
print(l)                   # [10, 111, 20, 30, 222, 40]
l.insert(10, 333)
print(l)                   # [10, 111, 20, 30, 222, 40, 333]
l.insert(-10, 444)
print(l)                   # [444, 10, 111, 20, 30, 222, 40, 333]

l1 = [1,2,3]
l2 = ['Rahul', 'Rakesh', 'Regina']
print('Before extend l1 is:', l1)
print('Before extend l2 is:', l2)
l2.extend(l1)
print('After extend l1 is:', l1)
print('After extend l2 is:', l2)

august_txns = [100, 200, 500, 600, 400, 500, 900]
sept_txns = [111, 222, 333, 600, 790, 100, 200]
print("August month transactions are : ",august_txns)
print("September month transactions are : ",sept_txns)
sept_txns.extend(august_txns)
print("August and Sept total transactions amount: ",sum(sept_txns))

n=[1, 2, 3]
n.remove(1)
print(n)

n=[1, 2, 3, 1]
n.remove(1)
print(n)

n=[1, 2, 3, 1]
n.remove(10)
print(n)                     #Value error

n=[1, 2, 3, 4, 5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)

n=[1, 2, 3, 4, 5]
print(n.pop(10))             #Index error

n=[1, 2, 3, 4, 'two']
print(n)
n.reverse()
print(n)

n=[1, 4, 5, 2, 3]
n.sort()
print(n)

s=['Suresh', 'Ramesh', 'Arjun']
s.sort()
print(s)

x=[10, 20, 30]
y=x                   #aliasing
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))

x=[10, 20, 30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))

x=[10, 20, 30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))

a= [1, 2, 3]
b= [4, 5, 6]
c = a + b
print(c)

a= [1, 2, 3]
b= 'Balu'
c = a + b
print(c)                      #Type error

a = [1, 2, 3]
print(a)
print(2*a)

print([1, 2, 3] < [2, 2, 3])
print([1, 2, 3] < [1, 2, 3])
print([1, 2, 3] <= [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])
print([1, 2, 3] < [0, 2, 3])
print([1, 2, 3] == [1, 2, 3])

x =["abc", "def", "ghi"]
y =["abc", "def", "ghi"]
z =["ABC", "DEF", "GHI"]
a =["abc", "def", "ghi", "jkl"]
print(x==y)
print(x==z)
print(x==a)

x=[10, 20, 30, 40, 50]
print(20 in x)                  # True
print(20 not in x)              # False
print(90 in x)                  # False
print(90 not in x)              # True

a = [80, 90]
b = [10, 20, 30, a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])

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

x = [1, 2, 3, 4]
y = []
for i in x:
    y.append(i*2)
print(y)

x = [1, 2, 3, 4]
y = [ i*2 for i in x]
print(y)

s=range(1, 20, 3)
for i in s:                    #This loop is for knowing what is in s
    print(i)
m=[x for x in s if x%2==0]     #List comprehension
print(m)

employee_ids = (1, 2, 3, 4, 5)
print("same type of objects:",employee_ids)
print(type(employee_ids))

employee_ids = 1, 2, 3, 4, 5
print("same type of objects:",employee_ids)
print(type(employee_ids))          #Parenthesis is optional for tuple

employee_details = (1, "RGV", 1000.123)
print("different type of objects:", employee_details)

name =("Sushanth")
print(name)
print(type(name))

a = (11)
print(a)
print(type(a))

name =("Sushanth",)
print(name)
print(type(name))

a = (11,)
print(a)
print(type(a))

emp_id = ()
print(emp_id)
print(type(emp_id))

emp_id = (11,)
std_id = 120,
print(emp_id)
print(std_id)

emp_id = (11, 12, 13)
std_id = 120, 130, 140
print(emp_id)
print(std_id)

l = [11, 22, 33]
t=tuple(l)
print(t)

t=tuple(range(1, 10, 2))
print(t)

t=(10,20,30,40,50,60)
print(t[0])             # 10 #Positive indexing
print(t[-1])            # 60 #Negative indexing
print(t[100])           # IndexError: tuple index out of range

t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2])

t=(10,20,30,40,50,60)
for i in t:
    print(i)

t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

t1=(10,20,30)
t2=t1*3
print(t2)

t=(10,20,30,40)
print(len(t))

t=(10,20,10,10,20)
print(t.count(10))

t=(10,20,10,10,20)
print(t.index(10))
print(t.index(30))         # ValueError

t=(40,10,30,20)
t1=sorted(t)
print(t)
print(t1)

t=(40,10,30,20)
t1=sorted(t,reverse=True)
print(t1)

t=(40,10,30,20)
print(min(t))             # 10
print(max(t))             # 40

a=10
b=20
c=30
d=40
t=a, b, c, d
print(t)

t=(10, 20, 30, 40)
a, b, c, d = t
print("a=",a , "b=" , b," c=", c ,"d=",d)

t= (x**2 for x in range (1,6))          #return generator object

t= ( x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)

d ={1:"Ramesh", 2:"Arjun", 3:"Nireekshan"}
print(d)

d = {}
d[1] = "Ramesh"
d[2] = "Suresh"
d[3] = "Mahesh"
print(d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d[1])                  #To access dictionary values we use key
print(d[2])            
print(d[3])

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d[10])                  #Key error

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
if 400 in d:
    print(d[400])
else:
    print("key not found")

d={}
n=int(input("Enter number of employees: "))
i=1
while i <=n:
    name=input("Enter Employee Name: ")
    salary=input("Enter Employee salary: ")
    d[name]=salary
    i=i+1
for x in d:
    print("The name is: ", x ," and his salary is: ", d[x])

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Old dictionary:", d)
d[10]="Hari"
print("Added key-value(10:Hari) pair to dictionary:",d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Old dictionary:", d)
d[3]="Hari"
print("UPdated value of key 3 pair to dictionary:",d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before deleting key from dictionary",d)
del d[1]
print("After deleting key from dictionary:", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before deleting key from dictionary",d)
del(d[10])
print("After deleting key from dictionary:", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before clearing dictionary: ", d)
d.clear()
print("After cleared entries in dictionary: ", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before clearing dictionary: ", d)
del d
print("After cleared entries in dictionary: ", d)       #Name error

d=dict()
print(d)
print(type(d))

d = dict({1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'})
print(d)

d = dict([(1, "Ramesh"), (2, "Arjun")])
print(d)

d = dict([(1, "Ramesh"), (2, "Arjun")])
print("length of dictionary is: ",len(d))

d = dict([(1, "Ramesh"), (2, "Arjun")])
print("length of dictionary is: ",len(d))

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d.get(1))
print(d.get(100))

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d.get(1))
print(d.get(100,'No key found'))

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before pop:", d)
d.pop(1)
print("After pop:", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
d.pop(23)                                 #Key error

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before popitem:", d)
d.popitem()
print("After popitem:", d)

d= {}
d.popitem()                                #Key error
print("After popitem:", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d)
for k in d.keys():
    print(k)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d)
for k in d.values():
    print(k)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
for k, v in d.items():
    print(k, "---", v)

d1 = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
d2=d1.copy()
print(d1)
print(d2)
print(id(d1))
print(id(d2))

squares={a:a*a for a in range(1,6)}
print(squares)
"""