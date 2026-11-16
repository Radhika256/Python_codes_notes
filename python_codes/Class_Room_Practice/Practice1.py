#syntax error=when interpreter not able to understand the code due to some syntax error
#runtime error/exceptions=when interpreter finds some error while executing the program
#logical error=when interpreter doesn't find any error but the program doesn't give the expected output

# Runtime error(end=user input)
# print(10/0)
# Runtime error(programming logic)
# print(10/"Two")

#Exception Handling
"""
print('One')
print('Two')
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception passed")
print('Four')
print('Five')

print('One')
print('Two')
try:
    print(10/0)
except ZeroDivisionError as z:
    print("Exception information:",z)
print('Four')
print('Five')

#error can be many but exception can only be one

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:")) 
    print(x/y)
except ZeroDivisionError:
    print("Can't divide with zero")
except ValueError:
    print("Please provide int value only")

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:")) 
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print("Please provide valid numbers only and problem is:",e)

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:")) 
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError: Can't divide with zero")
except:
    print("Default Except: Please provide valid input only")

try:
    print("try block")
except:
    print("except block")
finally:
    print("finally block")

try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("except block")
finally:
    print("finally block")

try:
    print("try block")
    print(10/0)
except NameError:
    print("except block")
finally:
    print("finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

try:
    print("outer try block")
    print(10/0)
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except NameError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

try:
    print("try block")
except:
    print("except: Handling code")
else:
    print("else block")
finally:
    print("finally block")

try:
    print("try block")
    print(10/0)
except:
    print("except: Handling code")
else:
    print("else block")
finally:
    print("finally block")

#Custom Exception in python

try:
    x=int(input("Enter a number between positive integer:"))
    if x<0:
        raise ValueError(x)
except ValueError as e:
    print("You provided {}. Please provide positive integer values only".format(e))

#Text file is a file that stores data in text format
#Binary file is a file that stores data in binary format
f=open("abc.txt",'w')
print("File Name:",f.name)
print("File Mode:",f.mode)
print("Is File Readable:",f.readable())
print("Is File Writable:",f.writable())
print("Is File Closed:",f.closed)
f.close()
print("Is File Closed:",f.closed)

f=open("wish.txt",'w')
f.write("Welcome\n")
f.write("to\n")
f.write("python world\n")
f.write("Data written to the file successfully")
f.close()

f=open("names.txt",'w')
list=["Ramesh\n","Arjun\n","Senthil\n","Vagnesh"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abc.txt",'r')
data=f.read()
print(data)
f.close()

f=open("abc.txt",'r')
data=f.read(20)
print(data)
f.close()

f=open("abc.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end="")
f.close()

f=open("abc.txt",'r')
line1=f.readline()
print(line1,end="")
line2=f.readline()
print(line2,end="")
line3=f.readline()
print(line3,end="")
f.close()

with open("test.txt","w") as f:
    f.write("Welcome\n")
    f.write("to\n")
    f.write("python\n")
    print("Is File Closed:",f.closed)
print("Is File Closed:",f.closed)

f=open("test.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
f.close()
"""
