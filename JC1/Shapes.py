#WRITE A PROGRAM (WITH SEPERATE FUNCTIONS) TO FIND THE PERIMETER AND AREA OF:
#1. CIRCLE
#2. RECTANGLE
#3. PARALLELOGRAM
#4. TRIANGLE
#5. SPHERE (VOLUME)

def areaCircle(radius):
    areaC = radius * radius * 3.14
    return areaC

def periCircle(radius):
    periC = 2 * radius * 3.14
    return periC

def areaRectangle(length, breadth):
    areaRect = length * breadth 
    return areaRect

def periRect(length,breadth):
    periRect = 2 * length + 2 * breadth
    return periRect

def areaParallel(base, height):
    areaPara = base * height
    return areaPara

def periParallel(length, breadth):
    periPara = 2 * length + 2 * breadth
    return periPara

def areaTriangle(base, height):
    areaTri = 0.5 * base * height
    return areaTri

def periTriangle(side1,side2,side3):
    periTri = side1 + side2 + side3
    return periTri

def areaSphere(radius):
    areaSph = 1.333 * radius * radius * radius * 3.14
    return areaSph

def periSphere(radius):
    periSph = 4 * 3.14 * radius * radius
    return periSph

RadiusC = int(input("enter radius of circle: "))
tempAC = areaCircle(RadiusC)
print ("the area of circle is", tempAC)     
tempPC = periCircle(RadiusC)
print ("the perimeter of circle is", tempPC)  


LengthR = int(input("enter Length of rectangle  : "))
BreadthR = int(input("enter Breadth of rectangle : "))
tempAR = areaRectangle(LengthR,BreadthR)
print ("the area of rectangle is", tempAR)     
tempPR = periRect(LengthR,BreadthR)
print ("the perimeter of rectangle is", tempPR)     

LengthP = int(input("enter Length of parallelogram  : "))
BreadthP = int(input("enter Breadth of parallelogram : "))
tempAP = areaParallel(LengthP,BreadthP)
print ("the area of parallelogram is", tempAP)     
tempPP = periParallel(LengthR,BreadthR)
print ("the perimeter of parallelogram is", tempPP)   

BaseT = int(input("enter Base of Triangle  : "))
HeightT = int(input("enter Breadth of Triangle : "))
tempAT = areaTriangle(LengthP,BreadthP)
print ("the area of Triangle is", tempAT)  
SideT1 = int(input("enter Side1 of Triangle  : "))
SideT2 = int(input("enter Side2 of Triangle : "))   
SideT3 = int(input("enter Side3 of Triangle : "))   
tempPT = periTriangle(SideT1, SideT2,SideT3)
print ("the perimeter of Triangle is", tempPT)   

RadiusS = int(input("enter radius of sphere: "))
tempAS = areaSphere(RadiusS)
print ("the area of sphere is", tempAS)     
tempPS = periSphere(RadiusS)
print ("the perimeter of sphere is", tempPS)  
