"""class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def audio(self):
        print("Sound of Animal")
class Bird(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Horse")
        self.breed = breed
    def audio(self):
        print("BARKS!!!")
A = Animal("Tejas","Mammal")
B = Bird("Tejas","Mammal")
B.audio()
A.audio()"""

class Super:
    def fun1(self):
        print("I am a parent class")
class child(Super):
    def fun2(self):
        print("I am a Child Class")
C = child()
C.fun1()
C.fun2()
