class Person:

    # Note: The self parameter is a reference to the current instance of the class,
    #  and is used to access variables that belong to the class.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Milad", 36)
print(p1.name)
print(p1.age)
p1.myfunc()
print(p1)


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self,
# you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example
# Use the words mysillyobject and abc instead of self:

class Person2:
    def __init__(mysillyobject, name, age):
        mysillyobject.nameNew = name
        mysillyobject.ageNew = age

    def myfunc(abc):
        print("Hello, my name is " + abc.nameNew)


p2 = Person2("Mili", 30)
print(p2.nameNew)
print(p2.ageNew)
p2.myfunc()

p2.ageNew = 40
print(p2.ageNew)
del p2.ageNew  # Delete Object Properties

# print(p2.ageNew) # AttributeError: 'Person2' object has no attribute 'ageNew'
print(p2)

del p1  # Delete Objects
