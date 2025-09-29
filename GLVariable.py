x = 97          #Global Variable
print(x)
def dell():
    global x    #Changing value of the global Variables
    x = 80       
    y = 30      #Local Variable
    print(y)
    print(x)
dell()
print(x)
