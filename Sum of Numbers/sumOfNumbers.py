a = []
t = 0
print('Write "c" to calculate the Total')
x = float(input("numbers to be total_"))
a.append(x)
t = t+x
while (x != "c"):
    x = (input("numbers to be total_"))
    if x != "c":
        x = float(x)
        a.append(x)
        t = t+x
k = 0
while k < len(a):
    if k != (len(a)-1):
        print(a[k], end=" + ")
    else:
        print(a[k])
    k += 1
print(t)
