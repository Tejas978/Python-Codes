print("Hello World")
 
'''def func():
    for i in range(500):
       yield i

obj1 = func()
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))

for j in obj1:
    print(j)'''

'''def fun():
    yield 2
for i in fun():
    print(i)'''

def list():
    for i in range(101):
        yield i

obj = list()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

for j in obj:
    print(j)