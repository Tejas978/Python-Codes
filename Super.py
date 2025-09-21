class teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student(teacher):
        def __init__(self,name,age,Branch):
          super().__init__(name,age)
          self.branch = Branch
          print(f"{self.name},{ self.age} and {self.branch}")

tej = student("Tejas",20,"IT")
print(tej)