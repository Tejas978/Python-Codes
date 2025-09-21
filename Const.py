class person:
    def __init__(self,Name,Occ):
        self.name = Name
        self.occ  = Occ
    def hello(self):
        print(f"{self.name} will work on {self.occ} ")
    
top = person("Tejas","Web Dev")
top.hello()
top = person("Rohan","Cyber Security")
top.hello()



