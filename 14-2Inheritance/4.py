from locale import LC_MONETARY


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object
# and then execute the printname method:


x = Person("John", "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname):
        # To keep the inheritance of the parent's __init__() function
        # add a call to the parent's __init__() function
        Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()
