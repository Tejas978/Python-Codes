#Local AND Global Variable
x = 10
T = "Tejas Khaire"

def hello(y):
    global x
    x = 20
    print(y*x)
hello(5)
