# Create a variable called age and assign the value 20 to it. Then write an if statement that prints "You are a teenager" if the value of age is less than 18, and "You are an adult" if the value of age is equal to or greater than 18.
# Create two variables called name and city. Then write an if statement that prints "You are from [city]" if the value of name is equal to "John" or "Jane", and "You are not from [city]" if the value of name is anything else.
# Create a variable called password and assign a value to it. Then write an if statement that checks if the length of password is less than 6 characters. If it is, then print "The password is too short". Otherwise, print "The password is long enough".
# Create a variable called number and assign a value to it. Then write an if statement that checks if number is positive, negative, or zero. If it is positive, print "The number is positive". If it is negative, print "The number is negative". If it is zero, print "The number is zero".
# Create two variables called x and y. Then write an if statement that prints "x is greater than y" if x is greater than y, and "y is greater than x" if y is greater than x.
# Create two variables called a and b. Then write an if statement that prints "a is equal to b" if a is equal to b, and "a is not equal to

age=20
if age<18:
    print("you are a teenager")
else:
    print("you are an adult")

name="Jane"
city="parma"
if name=="John" or name=="Jane":
    print(f"you are from {city}")
else:
    print(f"you are not from {city}")

password="123456"
if len(password)<6:
    print("The password is too short")
else:
    print("The password is long enough")

number=(-5)
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")

x=3
y=5
if x>y:
    print("x is greater than y")
else:
    print("y is greater than x")

a=10
b=10
if a==b:
    print("a is equal to b")
else:
    print("a is not equals to b")
