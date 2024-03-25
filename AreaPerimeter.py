#Write a program to calculate the area or perimeter of a circle. 
#Use procedures of functions for each of the following tasks. 
#1. Input and validate the radius
#2. calculate the area
#3. calculate the perimeter
#4. Output result
# Main program gives choice to calculate area or perimeter

def areaCircle(radius):
    areaC = radius * radius * 3.14
    return areaC

def periCircle(radius):
    periC = radius * 3.14 * 2
    return periC

def InputRadius():
    radius = int(input("enter radius: "))
    while radius <= 0:
        print ("cannot be 0 or negative..")
        radius = int(input("enter radius: "))
    return radius


radius = InputRadius()
choice = (input("calculate area or perimeter?: ")).lower()
if choice == "area":
    temp = areaCircle(radius)
    print (temp)
elif choice == "perimeter":
    temp = periCircle(radius)
    print (temp)
