list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
print(len(list1), len(tuple1), len(set1), len(dict1))
print(list1[0], tuple1[0])
print(dict1["lion"])
list1[2]="rabbit"
#tuple1[2]="rabbit" le tuple non possono essere modificate
list1.append("monkey")
list1.remove("rabbit")
dict1["fish"]=0
