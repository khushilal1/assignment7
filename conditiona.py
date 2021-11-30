

# if else statement
x =int(input("Enter the value of x:"))
if x%2==0:
    print("x is divisible by 2")
else:
    print("x  s not divisble by 2")


# use of elif and if statement
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
if x > y:
    print("x is gretaer than y")
elif x < y:
    print("x is smeller than y ")
elif x == 0:
    print("x is zero ")
elif y == 0:
    print("y is zero ")
else:
    print("x is equal to y")




x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
if x > y:
    print("x is gretaer than y")
elif x < y:
    print("x is smeller than y ")
elif x == 0 and y==0:
    print("x and y are zero ")
else:
    print("x is equal to y")


x=int(input("Enter the value of x:"))
if x%2==0:
    print("x is diviible by 2:")
else:
    print("x is not dicivsible by 2:")


x= int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

if x== y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')



# write a program to find thge saalry of a person working hours greter than 40 givees 1.5  more per hoour but les than 40 thatis given  10 per hour
h=float(input("Enter tyye hours does the worker work:"))
if(h>40):
    r=10*1.5*h
    print(f"the total payment of the worker be {r}")
else:
    r=10*h
    print(f"the total payment of the worker be {r}")
    

s = float(input("Enter the  your score:"))
if (s<= 1.0):
    if(s > 0.9 and s<=1.0):
        print(f"you have got  garde A for your garde {s}")
    elif(s >0.8 and s <=0.9):
        print(f"you have got  garde B for your garde {s}")
    elif(s >0.7 and s <=0.8):
        print(f"you have got  garde C for your garde {s}")
    elif(s >0.6 and s <=0.7):
        print(f"you have got  garde D for your garde {s}")
    elif(s <0.6):
        print(f"you have got  garde E for your garde {s}")
else:
    print("An error mewssage")




# write a program for the printing of thgw dgrade of students  as they entered their GPA


print("NEPAL GPA SYSTEM OF EDUCATION!!!\n")


s = float(input("Enter the  your score in GPA:\n"))
if (s<=4):
    if(s > 3.6 and s<=4):
        print(f"you have got  garde A+ for your garde {s}")
    elif(s >3.2 and s <=3.6):
        print(f"you have got  garde A for your garde {s}")
    elif(s >2.8 and s <=3.2):
        print(f"you have got  garde B+ for your garde {s}")
    elif(s >2.4 and s <=2.8):
        print(f"you have got  garde B for your garde {s}")
    elif(s >2.0 and s <=2.4):
        print(f"you have got  garde C+ for your garde {s}")
    elif(s >1.6 and s <=2.0):
        print(f"you have got  garde C for your garde {s}")
    elif(s >1.2 and s <=1.6):
        print(f"you have got  garde D+ for your garde {s}")
    elif(s >.8 and s <=1.2):
        print(f"you have got  garde D for your garde {s}")
    elif(s <=0.8):
        print(f"you have got  garde E for your garde {s}")
else:
    print("Please!!! Reacheck your GPA once more....")

