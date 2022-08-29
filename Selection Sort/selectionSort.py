list = [37, 42, 56, 63, 14, 35, 21, 62, 49, 70]

for i in range(len(list)-1):
    minimumvalue = i
    for j in range(i+1, len(list)):

        if list[j] < list[minimumvalue]:
            minimumvalue = j

    pseudo = list[i]
    list[i] = list[minimumvalue]
    list[minimumvalue] = pseudo

print(f"sorted List {list}")
