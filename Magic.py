class student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def __str__(self):
        return (f"I am from {self.name}")
    def __repr__(self):
        return (f"I am from {self.name}")
    def __call__(self):
        print ("Last of US")

obj = student("Tejas Khaire",202)
print(obj.name)
print(str(obj))
print(repr(obj))

obj()



