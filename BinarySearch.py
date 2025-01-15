#THE ARRAY MUST BE SORTED 
#1.) find the middle index use    mid <- INT((low+high)/2)
#2.) compare the mid with the search element
#3.) if not the same, we can find if the search element greater or less than the mid
#4.) IF myArr[mid] > SE THEN high <- mid-1
#5.) IF myArr[mid] < SE THEN low <- mid+1
#6.) Repeat the steps until found

myArr = [2,3,5,7,9,11,14,18,23]
found = False
flag = False
search = int(input("Please enter a number: "))
high = len(myArr)-1
low = 0


while found == False and flag == False:
    mid = (low+high)//2
    if myArr[mid] == search:
        found = True
    elif myArr[mid] > search:
        high = mid-1
    elif myArr[mid] < search:
        low = mid+1
    if low != high:
        flag = True

if found == False:
    print ("NOT FOUND")
else:
    print ("FOUND" )