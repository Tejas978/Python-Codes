class Super:
    def fun1(self):
        self.name = "Tejas"
        print("I am a parent1 class")
        print(f"My Name is {self.name}")
class Super1(Super):
    def fun2(self):
        print("I am a Parent2 class")
class child(Super):
    def fun3(self):
        print("I am a Child Class")
C = child()
S = Super1()
C.fun1()
S.fun1()

2 = "TEJAS"
print(2)