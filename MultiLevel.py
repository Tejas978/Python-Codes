class Super:
    def fun1(self):
        print("I am a parent1 class")
class Super1(Super):
    def fun2(self):
        print("I am a Parent2 class")
class child(Super1):
    def fun3(self):
        print("I am a Child Class")
C = child()
C.fun1()
C.fun2()
C.fun3()