fruits = {"apple","banana","cherry"}

# access

for x in fruits:
    print(x)

print(fruits)

# add item to set

fruits.add("orange")
print(fruits)

# add any iterable

winterfruits = ["Date","pulm","Date"]
fruits.update(winterfruits)

print(fruits)

#  remove item from set

fruits.remove('pulm')
print(fruits)