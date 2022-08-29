print("Marks sheet for class IX\n")

a = float(input("Enter Sindhi Obtained Marks : "))
b = float(input("Enter English Obtained Marks : "))
c = float(input("Enter PSt Obtained Marks : "))
d = float(input("Enter Biology Obtained Marks : "))
e = float(input("Enter Chemistry Obtained Marks : "))
f = float(input("Enter Total Marks of All Subjects : "))

if f != 0:
    g = a+b+c+d+e

h = float(g/f)*100
if f != 0 and f > g:
    print(h)
if h >= 80:
    print("Grade: A+")
if h >= 70 and h < 80:
    print("Grade: B")
if h >= 60 and h < 70:
    print("Grade: C")
if h >= 50 and h < 60:
    print("Grade: D")
if h >= 40 and h < 50:
    print("Grade: E")
if h >= 33.33 and h < 40:
    print("Grade: U")
if h < 33.33:
    print("Grade: F")
    print("Mate you are failed!!!")
