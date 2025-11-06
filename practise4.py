'''class student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
    def sinfo(self):
        print(f"My name is {self.name} and age is {self.age} from {self.branch}")
obj = student("Harry",25,"CSE")
print(obj.name)
obj.age = 30
print(obj.age)
print(obj.branch)
obj.sinfo()
print("Hello WORLD ")
obj1 = student("Tejas",30,"IT") 
obj1.sinfo()'''

'''class Padd:
    def add(a,b):
        X = a+b
class hello(Padd):
    def add(a,b):
     super().add(a,b)
    def add2(X):
        print(X)
obj = hello()
obj.add(6,4)

'''
"""a = 11
b = a*10
print(a,b)
"""
"""a = '10'
b = "20"
print(a+b)"""

'''list = [1,4,"Tejas",True]
result = list[1:2]
print(result)'''

'''dict = {"age":24,"Name":"Tejas Khaire","Branch":"IT"}
print(dict)
re = dict.index(0)
print(re)'''
 
list = ["Tejas",5,8]
print(list.index(5))
for i in list:
    print(i)