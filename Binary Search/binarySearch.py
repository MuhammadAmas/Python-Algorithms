list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
inp = int(input("Enter A number that you want to find :"))
start = 0
end = len(list)-1

flag = 0
while start < end and flag == 0:
    midpoint = (start+end)//2

    if list[midpoint] == inp:
        print(f"Number is found in the list at {midpoint+1}th position")
        flag = 1

    else:
        if list[midpoint] <= inp:
            start = midpoint+1
        if list[midpoint] >= inp:
            end = midpoint-1

    if list[start] == inp:
        print(f"Number is found in the list at {start+1}th position")
        flag = 1
    elif list[end] == inp:
        print(f"Number is found in the list at {end+1}th position")
        flag = 1
