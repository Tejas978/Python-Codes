class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def info(cls,string):
        return cls(string.split("$")[0],string.split("$")[1])
obj = student("Tejas Khaire",20)
print(obj.name)
print(obj.age)
string = "Harry$32"
obj1 = student.info(string)
print(obj1.name)
print(obj1.age)

