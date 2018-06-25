#question1
n=int(input("enter year"))
if(n%4==0):
    print("leap year")
else:
    print("not a leap year")

#question2
length=int(input("enter length:-"))
breadth=int(input("eneter breadth:-"))
if(length==breadth):
    print("dimensions of square")
else:
    print("dimensions of rectangle")

#question3
x=int(input("enter 1st age"))
y=int(input("enter second age"))
z=int(input("enter third age"))
if(x>y):
    print("first age is greater %d"%(x))
elif(y>z):
    print("second age is greater %d"%(y))
else:
    print("third age is greater %d"%(z))

#question4
point=int(input("enter your points"))
if(point<50):
    print("sorry! no prize this time")
elif(point<150):
    print("congratulations you have won wooden dog")
elif(point<180):
    print("congratulations you have won a book")
elif(point<200):
    print("congratulations u have won chocolate")
else:
    print("incorrect point")

#question5
qua=int(input("enter the quantity"))
cost=100
total=qua*cost
y=total*10//100
discount=total-y
if(total>1000):
    print("after discount rupees %d"%(discount))
else:
    print("no discount")

    


    
