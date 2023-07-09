x=input("print a number ")
y=input("print a number ")
if x>y:
    print("Firstnumber is greater")
elif x<y:
    print("Second number is greater")
else:
    print("Both numbers are equal")

a=2
b=3
c=4

if (a+b+c)%2==0:
    print ("The sum is even")
else:
    print("The sum is odd")

import datetime
year=int(input("print a year "))
diff=(datetime.datetime(year,3,1))-(datetime.datetime(year,2,1))
if diff.days==29:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
