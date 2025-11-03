'''print("Hello World")
print("Below Program is to Calculate CGPA For a Year ")
def cgpa():
   Sem1 = float(input("Enter 1: "))
   Sem2 = float(input("Enter 2: "))
   Pointer = (Sem1 + Sem2)/2
   print(Pointer)
cgpa()'''
'''
T = "Tejas"
print(T[0:4])
print(len(T))
print(T.upper())'''
'''
for i in T:
    print(i)
for i in T(1,4,2):
    print(i)'''
'''
print("AT your Service")
A = (input("Enter Day: "))
if (A == "Mon"):
    print("You can Drive")
elif(A  == "Sun"):
    print("If you Wnt To U Can")
else:
    print("Died")

''''''

T = int(input("Enter Your Num: "))
match T:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case 3:
        print("Case 3")
    case 4:
        print("Case 4")
    case _:
        print(T)'''
'''for i in range(1,100,2):
    i = i+1
    print(i)
p = 100
while(p>=100):
    print(i)
    i = (i+1)
    break
    ''''''
list = [0,1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[5])
print(list[0:10:2])
List = [i for i in range(0,5,2)]
print(List)
''''''
tuple = (0,1,2,3,4,5,6,7,8,9,10)
print(tuple[5:9:2])
print(len(tuple))
x = 48'''
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)
print(thistuple)

T = (1,2,3,4,5)
E = list(T)
E.append(6)
T = tuple(T)
print(E)
print(T)'''
'''
T = "Tejas"
K = "Khaire"
#print(f"My name is {T} and Surname is {K}")
print("My Name is ",T,"and My Surname is ",K)
T = "Tejas"
K = "Khaire"
print("My Name is ", T, "and My Surname is ", K)'''

#def mul(a,b):
'''These is a multiplication function'''
''' T = a*b
    print(T)
mul(8,8)
print(mul.__doc__)'''
'''def factorial(n):
   if (n==0 or n==1):
    return 1
   else:
    return n * factorial(n-1)
print(factorial(5))'''"""
def fibonacci(a):
  if (a == 0 ):
    return 0
  elif(a == 1):
    return 1
  else:
    return (fibonacci(a-2) + fibonacci(a-1))
print (fibonacci(15)) """
'''
a = {0,1,2,3,4,56,9,5,5,6,7,8,8}
b = {0,2,4,56,4,3,9,7,6,5,4}
'''
'''for i  in set:
    print(i)'''
'''i = 0
while i<10:
    print(set)
    i = i + 1'''

'''print(set.union(set1))
'''
'''print(a.update(b))'''
'''print(a)'''
'''print(a.intersection(b))
print(a.intersection_update(b))
print(a)
print(a.issuperset(b))
x = b.pop()
print(x)'''
'''
for i in range(10):
  
    if i == 2:
     continue
    print(i)
else:
    print("H")'''
#try:
'''b = int(input("Enter your index: "))
 a = [20,25,24,26,29,27,28,21,23,22]
 print(a[b])
except Exception as e:
 print("Invalid Content")'''

'''N = int(input("Enter Your Number: "))
if (10<N<18):
    raise ValueError("Movie is not suitable for below 18")
elif (19<N<38):
    print("Allowed to watch the movie")
else:
    print("Game Over")
'''
'''
x = int(input("Enter your Num: "))
result = "A" if 80<x<100 else "Study" if 0<x<32 else "Save"
print(result)'''

'''list = [30,29,28,27,26,25,24,23,22,21]
for i in list:
    print(i)
for i in enumerate(list,start=1):
    print(i)'''
'''
import Imeg2
Imeg2.hello()'''
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')


class student:
    Name = "Tejas"
    Age = 21
    Roll = 81
    Branch  = "IT"
    Div = 'B'

obj1 = student()
print(obj1.Name)
obj1.Name = "Harry"
print(obj1.Name)
obj2 = student()
print(obj2.Age)








