# Given a string sentence = "The quick brown fox jumps over the lazy dog.", calculate and print the number of vowels in the sentence.
# Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create and print a new list that contains only the odd numbers.
# Given a list mixed = [1, "apple", 3, "banana", 5, "cherry"], create and print two separate lists, one containing the numbers and one containing the strings.
sentence = "The quick brown fox jumps over the lazy dog."
vowels=sentence.count("a")+sentence.count("e")+sentence.count("i")+sentence.count("o")+sentence.count("u")
print(vowels)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list=[]
for x in numbers:
    if x%2!=0:
        list.append(x)
print(list)
mixed = [1, "apple", 3, "banana", 5, "cherry"]
listnumber=[]
liststrings=[]
for x in mixed:
    if type(x) ==str:
        liststrings.append(x)
    elif type(x)==int:
        listnumber.append(x)
print(listnumber)
print(liststrings)