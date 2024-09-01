thisdict = {
    "name":"Mark Manson",
    "professon": "Author and youtube",
    "country": "Unites States"
}

print(thisdict)

#  update the dictionary

thisdict["books"] = ["Subtle art of not giving a f*ck ", "chase"]
print(thisdict)
thisdict["books"] = ["Subtle art of not giving a f*ck ", "Every this is f*cked up"]
print(thisdict)

#  number of items in dictionary
print(len(thisdict))
# data type
print(type(thisdict))

# access items

x = thisdict["books"]

print(x)

myKeys = thisdict.keys()
print(myKeys)


dicItems = thisdict.items()
print(dicItems)

thisdict["state"] = "Philly"
print(dicItems  )

thisdict.update({"rating":35})
print(thisdict)

# remove items

print(thisdict.pop("rating"))

print(thisdict.popitem())