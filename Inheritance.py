class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f"{self.name} has id no. {self.id}")
class hello(student):
    def lang(self) :
        print("I love Python")

r = student("Tejas","VU4F2223081")
r.details()
t = hello("Harry",45)
t.details()
t.lang()

