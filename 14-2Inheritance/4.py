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
        # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
        super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname()
