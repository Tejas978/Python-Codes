import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func1(n):
    print(f"Time Taken is {n}")
    time.sleep(n)
    return n
def poolingDemo():
    with ThreadPoolExecutor() as executor:
       ''' t1 = executor.submit(func1,4)
        t2 = executor.submit(func1,3)
        t3 = executor.submit(func1,1)
    print(t1)
    print(t2)
    print(t3)'''
       l = [5, 4, 6, 2]
       result = executor.map(func1, l)
       for R in result:
         print(R)
poolingDemo()