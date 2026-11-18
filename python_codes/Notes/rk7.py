#Standard Packages=cs,sys,math,random,datetime,collections,itertools
#file Handling is just like reading and writing(work from inside) but file manupulation is deleting,copying(wording from outside)
"""
import os

print(os.getcwd())
os.chdir('c:/tmp')
print(os.listdir('.'))
os.mkdir('demo/sub',exist_ok=True)
print(os.path.join('demo','abc.txt'))

import sys
print(sys.version)
print(sys.argv)
print(sys.path)
sys.exit(0)

from math import *
print(sqrt(45))
print(ceil(12.00001))                   #13
print(floor(12.99999))                  #12
print(round(12.4567,2))                 #To round off in decimal part
print(round(12454.4567,-2))             #To round off in integer part
print(pow(2,3))
print(log(100,10))                      
print(log(e))
print(sin(radians(30)))
print(degrees(atan(1)))
print(sin(30*(3.14/180)))
print(sin(30*((22/7/180))))
print(sin(30*(pi/180)))

import random
print(random.randint(1,10))
print(random.random())                         #Random float in (0.0,1.0)
num=[1,4,3,7,2]
print(random.choice(num))
random.shuffle(num)
print(num)

import datetime
now=datetime.datetime.now()
print(now)
formatted=now.strftime("%Y-%M-%D %H:%M:%S")
print("Formatted:",formatted)

tomorrow=now+datetime.timedelta(days=1)
print("Tomorrow:",tomorrow.date())

from collections import Counter, defaultdict, deque
c=Counter("banana")
print(c)
dd=defaultdict(int)
dd['x']+=1
print(dd['x'],dd['y'])
print(dd.keys())

from collections import Counter, defaultdict, deque
dq = deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(dq)
print(type(dq))

from collections import namedtuple

Person = namedtuple('Person',['name','age','city'])
p1=Person('Alice',30,'New York')
p2=Person(name='Bob',age=25,city='London')
print(p1.name,p1.age,p1.city)                              #Accessing by name
print(p2[0],p2[1],p2[2])                                   #Accessing by index
name,age,city = p1
print(name,age,city)
"""
