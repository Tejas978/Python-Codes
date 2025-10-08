def my_gen():
    for i in range(4):
        yield i
gen = my_gen()
'''print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))'''

for j in gen:
    print(j)
