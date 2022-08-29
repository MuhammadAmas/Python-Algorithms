def pwr(a, b):
    if b == 0:
        return (1)
    else:
        return (a*pwr(a, b-1))


a = int(input("Enter Base Value :"))
b = int(input("Enter Exponent Value :"))
n = pwr(a, b)
print(n)
