student = ["Sam","Mira","Josua","Peter","Sam"]

print(student)

print(len(student))

# access elemenst
print(student[1])
print(student[-1])
print(student[0:3])

# perform checking

if 'Sam' in student:
    print("Sam is a student")

# modification

student[1] = "Mira Murati"
print(student)

student[0:3] = ["Sam Altman","Mira Murati","Josua Bloch","Mark"]
print(student)

#adding and removing elements

student.append("Parag")

print(student)
student.insert(0,"Jeff")
student.insert(0,"Larry")
print(student)

indianSudent = ["Gaurav"]

student.extend(indianSudent)
print(student)

student.remove("Peter")
print(student.pop(6))
print(student)

# loops

for std in student:
    print(std)

i = len(student)
print(i)
while i > 0:
    print("inside while loop")
    print(student[i-1])
    i = i-1

for i in range(len(student)):
    print(student[i])

# list comprehenssion

[print(x) for x in student ]  

studentwithnameM = [x for x in student if 'M' in x]

print(studentwithnameM)

# sorting
student.sort()
print("sorted students")
print(student)

student.sort(reverse= True)
print(student)












