"""
s = {10,20,30,40}
print(s)
print(type(s))

s = {10,'20','Rahul', 234.56, True}
print(s)
print(type(s))

s=set(range(5))
print(s)

d={}                         #Empty Dictionary
print(d)
print(type(d))
s=set()                      #Empty Set
print(s)
print(type(s))

s={10,20,30}
s.add(40)
print(s)

s = {10,20,30}
l = [40,50,60,10]
s.update(l)
print(s)

s = {10,20,30}
l = [40,50,60,10]
s.update(l, range(5))
print(s)

s.add(10)           #Valid
s.add(10,20,30)     #Invalid, TypeError: add() takes exactly one argument (3 given)
s.update(10)        #Invalid, TypeError: ‘int’ object is not iterable
s.update(range(1,10,2),range(0,10,2))  #Valid

s={10,20,30}
s1=s.copy()
print(s1)

s = {40,10,30,20}
print(s)
print(s.pop())
print(s)

s={40,10,30,20}
s.remove(30)
print(s)

s={40,10,30,20}
s.remove(50)
print(s)

s={10,20,30}
s.discard(10)
print(s)

s={10,20,30}
s.discard(10)
print(s)
s.discard(50)
print(s)

s={10,20,30}
print(s)
s.clear()
print(s)

x={10,20,30,40}
y={30,40,50,60}
print(x.union(y))

x = {10,20,30,40}
y = {30,40,50,60}
print(x.intersection(y))
print(x&y)

x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y))
print(x-y)
print(y-x)

x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)

s= {1, 2, 3, "Sharuk"}
print(s)
print(1 in s)
print('S' in s)
print(2 not in s)

s = {x*x for x in range(5)}
print(s)

l=[10,20,30,10,20,40]
s=set(l)
print(s)

vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print(fSet)
print(type(fSet))
"""