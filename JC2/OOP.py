#Like a record but with functions, RECORD STRUCTURE:
#An object is an instance of a class. ----- INSTANTIATION
#Creating an object ---- CONSTRUCTION
#Constructor is a special method used to contruct objects. Allows you to create personalised objects while creation. 

#Abstraction

#Encapsulation: to group together the data and all the actions of the data. Hiding the data.

#Inheritance: 
    # Teacher (Child class / sub class) is a Person (Parent Class / Super class)
    # Student is a Person 
    # if the parent class attribute is private, cannot be directly accessed, so use getters and setters
    # Multiple inhertance = one subclass inherits from multiple super classes

#Polymorphism: is when a method (subclass) redefines a method from its parent class to add additional functionality

#Method overriding: allows you to have multiple mthods with the same name, diff num, types or order of arg

# in the same class, if have two of he same methods. --> method overriding
# if inherited by another class --> polymorphism




#Instance = Object
#Instance variable = The variables of the object, may differ for each object (self.)
#Non-instance variables / Class variables = The variables that belong to all objcets in the class (outside __init__)



#----------------------------------------------------

class Car:  #Record Data Structure TYPE DECLARATION

    make = ""
    model = ""
    color = ""

Car1 = Car()
Car1.make = "TOYOTA"
Car1.model = "2001"
Car1.color = "Blue"


'''
Type Car:
    DECLARE make: STRING
    DECLARE model: STRING
    DECLARE color: STRING

DECLARE Car1: Car
car1.make = "TOYOTA"
car1.model = "2001"
car1.color = "Blue" 
'''

#----------------------------------------------------

class Student:  #CLASS DECLARATION, useuppercase for first letter

    def __init__(self, name, subject, gender):
        self.name = name #this is parameter
        self.subject = subject
        self.gender = gender

    def introduction(self):  #when calling the method, PASS self to avoid error
        print(f"hello! ^3^ I am {self.name}, {self.gender} and my favourite subject is {self.subject}!!!")


Emily = Student("Emily","Physics","Female") 
# Emily.introduction()

Nadine = Student("Nadine","Biology","Female") 
# Nadine.introduction()


class Person:

    personCount = 0 #Class Variable / non-instance variable

    def __init__(self,name,DOB,gender): #Constructor
        self.__name = name #of type string       #self.name is an instance variable    #self.__name is a private variable, cannot be accessed
        self.__DOB = DOB #of type date
        self.__gender = gender #of type string
        Person.personCount += 1

    def walk(self):
        print(f"{self.__name} is now walking!! :D")

    def Run(self):
        print(f"{self.__name} is now running!! D:")
    
    def printDetails(self):
        print(f"Name is {self.__name}, Date of Birth is {self.__DOB}, Gender is {self.__gender}")

    
    #getters
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__DOB
    def getGender(self):
        return self.__gender        
    #setters
    def setName(self, name):
        self.__name = name
    def setDOB(self,DOB):
        self.__DOB = DOB
    def setGender(self,gender):
        self.__gender = gender       



Emily = Person("Emily","25/11/2007", "Female") #Instantiating
Nadine = Person("Nadine","07/08/2008", "Male")
Gichelle = Person("Gichelle","14/07/2008", "Female")
# Emily.Run()           
# Emily.walk()

# print(Nadine.__name) #doesn't work if private
# print(Nadine.__DOB)
# print(Nadine.__gender)
# print(Nadine.__dict__)       #dictionary format
# print(Person.personCount)

# print(Nadine.getName())
# print(Nadine.getDOB())
# print(Nadine.getGender())

# print(Nadine.__dict__)       #dictionary format
# print(Person.personCount)


# Emily.setName("Gichelle")
# Emily.printDetails()

#----------------------------------------------------

class Teacher (Person):
    def __init__(self, name, DOB, gender, subject, salary):
        super().__init__(name,DOB,gender)
        self.__subject = subject
        self.__salary = salary

    def getSubject(self):
        return self.__subject

    def getSalary(self):
        return self.__salary
    
    def printDetails(self):
        # print(f"Name is {self.__name}, Date of Birth is {self.__DOB}, Gender is {self.__gender},  Salary is {self.__salary}") # CANNOT ACCESSED BECAUSE ITS PRIVATE
        print(f"Name is {self.getName()}, Date of Birth is {self.getDOB()}, Gender is {self.getGender()},  Salary is {self.__salary}")
    
    
MrKhan = Teacher("Khan", "20/07/1999", "Male","CS","$100")
print("My subject is ", MrKhan.getSubject())
MrKhan.printDetails()

class Student(Person):
    def __init__(self,name,DOB, gender, grade):
        super(). __init__(name,DOB,gender)
        self.grade = grade

    def printDetails(self):
        print(f"Name is {self.getName()}, Date of Birth is {self.getDOB()}, Gender is {self.getGender()},  Grade is {self.grade}")



Gichelle = Student("Gichelle", "19/06/2008", "Female", "FFF")
Valerie = Student("Valerie", "05/05/2008", "Female", "ABC")
Gichelle.printDetails()
Valerie.printDetails()