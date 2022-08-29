x = int(input("year \n"))
l = x % 4
m = x % 100
n = x % 400
if (l == 0):
    if (m == 0):
        if (n == 0):
            print("x is a leap year")
        else:
            print("x is not a leap year")
    else:
        print("x ix a leap year")
else:
    print("x is not a leap year")
print("program has finished")
