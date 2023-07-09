# Create a string variable quote.
# Use string slicing to extract a specific word from the string (e.g., "is" from "This is a quote.")
# Use string methods to change the case of the string (e.g., upper, lower, title).
# Use string methods to remove specific characters from the string (e.g., replace, strip)
# Use string formatting to insert a variable into the string (e.g., {})

quote=" This is a quote "
print(quote[6:8])
print(quote.lower())
print(quote.upper())
print(quote.title())
quote=(quote.replace(" is", " was"))
print(quote.strip())
quote2="these are {} quotes".format(3)
print(quote2)

