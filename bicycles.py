# A list is a collection of items. You can store any number of items in a list, and they can be of any data type.
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
# Indexing in a list starts at 0 not 1. If you want to access an element in the list, you simply reduce one from the position of the element.
print(bicycles[0])
# You can perform any operations that you'd normally perform on a variable on an element of the list.
print(bicycles[1].upper())
print(bicycles[2].lower())
print(bicycles[3].title())

# Using negative index numbers to access the last element of the list
print(bicycles[-1])
# This method is useful if you have toaccess the last element of the list, but don't know the length of the list
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

# Using f strings to format the output
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

