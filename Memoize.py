from functools import lru_cache
import time
@lru_cache(maxsize =None)
def fx(n):
    time.sleep(4)
    return n*2

print(fx(5))
#print("Hello 5")
print(fx(10))
#print("Hello 10")
print(fx(15))
#print("Hello 15")

print(fx(5))
print("Hello 5")
print(fx(10))
print("Hello 10")
print(fx(15))
print("Hello 15")
