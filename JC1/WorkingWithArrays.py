StudentNames = [None for counter in range (10)] #studentNames is a str array of 10 elements
Studentmarks = [0 for counter in range (10)]

for Index in range(0,10):
    StudentNames[Index] = input("Please enter the name: ")
    Studentmarks[Index] = input("Please enter the marks: ")

for Index in range(0,10):
    print (StudentNames[Index])
    print (Studentmarks[Index])

print (StudentNames)
print (Studentmarks)

searchstudent = input("enter the name you want to search: ")
found = False
for Index in range(5):
    if searchstudent == StudentNames[Index]:
        found = True
        position = Index

if found == True:
    print(f"{searchstudent} scored {Studentmarks[Index]} was found at {position}")
else:
    print ("not present")
