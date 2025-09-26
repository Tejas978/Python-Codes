print("Hello World")
num = [1,2,3,4,5,6,7,8]
#MAP

lmap = map(lambda x: x*x,num)
print(list(lmap))

#filter

fmap = filter(lambda x : x%2==0 ,num)
print(list(fmap))

#reduce
from functools import reduce

fred = reduce(lambda x,y: x+y,num)

print(fred)




