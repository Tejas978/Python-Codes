class student:
    com = "Microsoft"               #CLASS Variable
    def __init__(self,name,exp):
        self.name = name
        self.exp  = exp
        self.prof = 2000            #Instance Variable
 
    def info(self):
        print(f"My Name is {self.name} and have {self.exp} of experience and raise amount is {self.prof} at {self.com}" )
obj1 = student("Tejas","2yr")
obj1.info()
obj2 = student("Harry","5yrs")
obj2.prof = 5000
obj2.info()

print("Hello World")