class student:
    branch = "IT"  
    def stud(self,name):
        self.name = name
    def info(self):
        print(f"My Name is {self.name} and my Branch is {self.branch}")
    @classmethod
    def show(cls,Branch):
        cls.branch = Branch
obj = student()
obj.stud("Tejas Khaire")
obj.info()
obj.show("CSE")
obj.info()