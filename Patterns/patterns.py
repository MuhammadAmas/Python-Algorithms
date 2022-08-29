print("R for \n*\n**\n***\n" + "S for \n***\n**\n*\n" + "T for Triangle of *\n")
# print("S for \n***\n**\n*")
# print("S for Triangle of *")


inp = input("what kind of stars you want to print?_")

# Making right triangle of "*"
if inp == "R":
    a = int(input("How many rows do you want?_"))
    b = "*"
    for k in range(a):
        print(b)
        b += "*"

# Making right triangle of "*" in inverse
if inp == "S":
    a = int(input("How many rows do you want?_"))
    for i in range(a, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print("\n")

# Making Triangle of *
if inp == "T":
    a = int(input("How many rows do you want?_"))
    for i in range(a):
        for k in range(1, a-i):
            print(" ", end="")

        for j in range(1, ((2*i)+2)):
            print("*", end=" ")
        print("\n")
