sentence="Laura and tom went ON a long walk."
sentence=sentence.lower()
sentence=sentence.capitalize()
sentence.replace("tom", "Tom")
sentence=sentence.replace("long","LONG")
sentence=sentence.replace("walk","wolk")
print(sentence)
print(sentence.split(" "))