class Super:
    def fun1(self):
        print("I am a parent class")
class Super1:
    def fun3(self):
        print("I am a Super1 class")
class child(Super,Super1):
    def fun2(self):
        print("I am a Child Class")
C = child()
C.fun1()
C.fun2()
C.fun3()
