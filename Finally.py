def T():
 try:
    a = [1,2,3,4,5]
    b = int(input("Enter Your Index: "))
    print(a.index(b))
    return 1
 except ValueError:
    print("Invalid Value")
    return 0
 finally:
    print("I will Always Execute")

print(T())


