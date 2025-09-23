import time
'''def forloop():
    for i in range(100):
        print(i+1)
def whileloop():
    i = 0
    while i<100:
     i = i+1
     print(i)

init = time.time()
forloop()
T1 = time.time() - init
init = time.time()
whileloop()
T2 = time.time() - init
print(T1)
print(T2)
'''

'''print("Let Me Check for your Documents")
time.sleep(5)
print("Sorry no documents are available")'''

u = time.localtime()
newtime = time.strftime("%d-%m-%Y\n %H:%M:%S",u)
print(newtime)
