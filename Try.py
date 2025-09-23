print("Hello World")
'''
a = input("Enter Your Number: ")
try:
  for i in range(1,11):
    print(f"Multiplication of {int(a)} X {i} = {int(a)*(i)}" )
except Exception as e:
   print(e)


print("The Codes Ends Here ")
print("Good Night")
'''
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except Exception as e:
    print("Number entered is not an integer.")