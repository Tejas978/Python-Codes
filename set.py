'''print("Hello WORLD")
T = {0,2,3,4,4,5,6,6,7,8,5,35,3}
print((T))

H = {"Now",4,54}
print(H)

for i in T:
    print(i)
 
#Mehods in Sets:-
A = {1,4,3,6}
B = {3,4}
print(A.symmetric_difference(B))
print(A.isdisjoint(B))
print(A.issuperset(B))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Delhi", "Seoul"}
cities.update(cities2)
print(cities)
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(item)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)