list = []
takinginput = (input("Enter the Nmbers you want to sort :"))
list.append(takinginput)
while takinginput != "break":
    takinginput = (input("Enter the Nmbers you want to sort :"))
    if takinginput != "break":
        list.append(takinginput)
print(f"Unsorted list {list}")

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            t = list[i]
            list[i] = list[j]
            list[j] = t
print(f"Sorted List {list}")
