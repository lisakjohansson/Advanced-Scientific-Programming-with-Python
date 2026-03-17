class Person:

    def __init__(self, firstname, lastname):

        "Constructor for this class "

        # Create person with firstname and lastname
        self.firstname = firstname
        self.lastname = lastname
    
    def getFullName(self):
        return self.firstname + " " + self.lastname
    
    def __str__(self):
        return self.getFullName()

class Student(Person):

    def __init__(self, firstname, lastname, subject):

        # Call parent constructor
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(self)
    
    def __str__(self):
        return self.getFullName() + ", " + self.subject


class Teacher(Person):

    def __init__(self, firstname, lastname, course):

        # Call parent constructor
        super().__init__(firstname, lastname)
        self.course = course

    def printNameCourse(self):
        print(self)
    
    def __str__(self):
        return self.getFullName() + ", " + self.course