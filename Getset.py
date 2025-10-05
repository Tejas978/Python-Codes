class person:
    def __init__(self,first):
        self.value = first
    def show(self):
        print(f"The Value is {self.value}")
    @property
    def tenX(self):       #Getter Function...
        return 10*(self.value)
    @tenX.setter          #Setter Function
    def tenX(self,second):
        self.value  = second
        return second/10
obj = person(10)
'''obj.value = 20
#obj.value
print(obj.tenX)     '''       #Getter...
obj.tenX = 67
print(obj.tenX)
obj.show()
































































