"""
num = 1
print("num==1 condition gives: ", (num==1))
if num == 1:
    print("if block statements executed")

num = 1
print("num==1 condition gives: ", (num==1))
if num == 1:
   print("if block statements executed")
else:
    print("else block statements executed")

print("Please enter the values from 0 to 4")
x=int(input("Enter a number: "))
if x==0:
    print("You entered:", x)
elif x==1:
    print("You entered:", x)
elif x==2:
    print("You entered:", x)
elif x==3:
    print("You entered:", x)
elif x==4:
    print("You entered:", x)
else:
    print("Beyond the range than specified")

x=int(input("Enter a number: "))
if x<0:
    print("The number is negative number")
else:
    print("The number is positive number")

user_name = 'rahul'
x=input("Enter a name: ")
if user_name == x:
    print("The name is valid")
else:
    print("The name is invalid")

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
if x>y :
    print("Biggest Number is: ", x)
else :
    print("Biggest Number is: ", y)

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
if x>y and x>z:
    print("Biggest Number is: ", x)
elif y>z :
    print("Biggest Number is: ", y)
else:
    print("Biggest Number is: ", z)

a, b = 10, 20
min = a if a < b else b
print(min)

x=1
while x<=5:
    print(x)
    x+=1
print("End")

x=10
while (x>=10) and (x<=20):
    print(x)
    x+=2
print("End")

x = [10, 20, 30, "Python"]
for i in x:
    print(i)

items_costs = [10, 20, 30,]
gst = 2
for x in items_costs:
    print(x+gst)

x= "python"
for ch in x:
    print(ch)
    
for x in range(1, 5):
    print(x)

item_costs = [10, 20, 30]
sum=0
for x in item_costs:
    sum=sum + x
print(sum)

rows = range(1, 5)
for x in rows:
   for star in range(1, x+1):
     print('*', end=' ')
   print()

group = [1, 2, 3, 4]
search = int(input("Enter the element in search: "))
for element in group:
    if search == element:
        print("element found in group")
        break

cart=[10, 20, 500, 700, 50, 60]
for item in cart:
    if item>=500:
        continue
    print("Item: ",item)

group = [1, 2, 3, 4]
search = int(input("Enter the element in search: "))
for element in group:
    if search == element:
        print("element found in group")
        break
else:
    print("Element not found")

def myfunction():
    pass

class Person:
    pass

total = 0                           # loop will run at least once
while True:
    num = int(input("Enter a number (or 0 to exit): "))
    if num == 0:
        break
    total += num
print("Total:", total)
"""
