import threading
import time

def func1(n):
    print(f"Time Taken is {n}")
    time.sleep(n)
   

'''func1(4)
func1(2)
func1(1)'''
t1 = threading.Thread(target = func1,args = [4])
t2 = threading.Thread(target = func1,args = [2])
t3 = threading.Thread(target = func1,args = [1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()