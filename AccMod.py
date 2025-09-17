# PUBLIC access Modifier
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"{self.name} and {self.age}")

obj = student("Tejas Khaire",20)
print(obj.name)
print(obj.age)

# PRIVATE access Modifier
class student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def hello(self):
        print(f"{self.name} and {self.age}")

obj = student("Tejas Khaire",20)
print(obj._student__name)
print(obj._student__age)

# PROTECTED access Modifier
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())