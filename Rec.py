'''def Factorial(n):
    if (n==0 or n==1):
        return (1)
    else:
        return (n * Factorial(n-1))

print(Factorial(5))'''

def Fiboo (n):
    if (n==0 ):
        return 0
    elif(n==1):
        return 1
    else:
       return Fiboo(n-2) + Fiboo(n-1)
print(Fiboo(3))