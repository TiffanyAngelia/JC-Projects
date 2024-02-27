#Number = int(input("enter number: "))

#if Number == 1:
    #print ("Sunday")
#elif Number == 2:
    #print ("Monday")
#elif Number == 3:
    #print ("Tuesday")
#elif Number == 4:
    #print ("Wednesday")
#elif Number == 5:
    #print ("Thursday")
#elif Number == 6:
    #print ("Friday")
#elif Number == 7: 
    #print ("Saturday")
#else: print ("error!")

Number = int(input("enter number: "))

match Number:
  case 1: print("Sunday")
  case 2: print("Monday")
  case 3: print("Tuesday")
  case 4: print("Wednesday")
  case 5: print("Thursday")
  case 6: print("Friday")
  case 7: print("Saturday")
  case _: print("error!")
