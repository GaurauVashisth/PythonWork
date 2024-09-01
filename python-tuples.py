thistuple = ("apple","banana","grapes","cherry")

print(thistuple)

# length of tuple

print(len(thistuple))
# access tuple items

print(thistuple[-1])

print(thistuple[1:3])
 # modify tupe
fruitlist = list(thistuple)
print(fruitlist)

fruitlist[0] = "Apple"

newTuple = tuple(fruitlist)

print(newTuple)

oneTuple = ("orange",)

oneTuple += newTuple

print(oneTuple)

# unpacking a tuple

# (a,b,c) = thistuple

# print(a)

# loop

for x in thistuple:
    print(x)

for x in range(len(thistuple)):
    print(thistuple[x])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i +1







