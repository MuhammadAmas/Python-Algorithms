marks = [100, 99, 98, 97, 96, 44, 55, 66, 77, 88, ]

# sorting marks
for i in range(len(marks)):
    min = i
    for j in range(i+1, len(marks)):
        if marks[j] < marks[min]:
            min = j
    t = marks[i]
    marks[i] = marks[min]
    marks[min] = t
print(marks)

# printing top 5 marks
a = 1
for k in range(5):
    print(f" At Number {a} {marks[k]}")
    a += 1

# printing last 5 marks
l = (len(marks)+1)-6
i = 5
for o in range(l, len(marks)):
    print(f" At {i} Last {l+1} {marks[l]}")
    l += 1
    i -= 1
