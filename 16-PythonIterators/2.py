mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
mymy = iter(mytuple)

print("myit", myit)
print("mymy", mymy)
print("mymy", iter(mytuple))

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit2 = iter(mystr)

print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))

print()

mytuple2 = ("1", "2", "3", "5", "4")

for x in mytuple2:
    print(x)

print()
mystr = "banana"

for x in mystr:
    print(x)
