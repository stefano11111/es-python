letter=input("print a letter ")
vowels=["a", "e", "i", "o", "u"]
if letter in vowels:
    print ("the letter is a vowel")
else:
    print("the letter is a consonant")

number=int(input("print a number "))
if number>0:
    print("The number is positive")
elif number<0:
    print("the number is negative")
else:
    print("the number is zero")

if number%5==0 and number%11==0:
    print("the number is divisible by 5 and by 11")
else:
    print("the number is not divisible by 5 and 11")

