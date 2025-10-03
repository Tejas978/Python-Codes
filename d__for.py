class myclass:
    def __init__(self,Name,Age):
        self.name = Name
        self.age  = Age

student = myclass("Tejas",20)
# print(student.name)
print(dir(myclass))
print(student.__dict__)
print(help(student))