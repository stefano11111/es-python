# Given two variables a = 3 and b = 4, calculate the integer of dividing b/a.
# Given two variables a = 3 and b = 4, calculate the reminder of and integer from dividing b/a.
# Given a list numbers = [3, 5, 7, 9, 11], calculate and print the sum of all elements in the list.
# Given a list grades = [83, 85, 72, 63, 95], calculate and print the average grade.
# Given a list prices = [5, 10, 15, 20, 25], calculate and print the highest and lowest price.

a = 3
b = 4
print(int(b/a))
reminder=b%a
print(reminder)
numbers = [3, 5, 7, 9, 11]
print(sum(numbers))
grades = [83, 85, 72, 63, 95]
media=sum(grades)/len(grades)
print(media)
prices = [5, 10, 15, 20, 25]
print(max(prices))
print(min(prices))