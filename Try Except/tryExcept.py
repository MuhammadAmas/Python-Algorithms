# example 1
a = float(input("Enter numerator :"))
b = float(input("Enter denominator :"))
if b != 0:
    c = (a/b)
    print(c)
else:
    print("numerator can't be zero")


# example 2
a = float(input("Enter numerator :"))
b = float(input("Enter denominator :"))
try:
    c = (a/b)
    print(c)
except:
    print("Error")
