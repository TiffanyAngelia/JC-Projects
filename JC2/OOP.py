#Like a record but with functions, RECORD STRUCTURE:
#An object is an instance of a class. ----- INSTANTIATION
#Creating an object ---- CONSTRUCTION
#Constructor is a special method used to contruct objects. Allows you to create personalised objects while creation. 

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
Emily.introduction()

Nadine = Student("Nadine","Biology","Female") 
Nadine.introduction()



#Encapsulation: to group together the data and all the actions of the data. 


