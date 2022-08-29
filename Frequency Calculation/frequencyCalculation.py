# opening text file.
file = open("text.txt", "r")
read = file.read()

# Creating a list of 256 elements
list = []
for a in range(256):
    list.append(0)

# Converting Characters into ASCII codes.
for i in read:
    convert = ord(i)
    list[convert] += 1

# Converting ASCII codes into characters
for b in range(256):
    if list[b] != 0:
        reconvert = chr(b)
        print(reconvert, list[b])
