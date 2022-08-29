def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot_element = list.pop()
    greaternumbers = []
    lowernumbers = []

    for numbers in list:
        if numbers > pivot_element:
            greaternumbers.append(numbers)
        else:
            lowernumbers.append(numbers)
    return quick_sort(lowernumbers) + [pivot_element] + quick_sort(greaternumbers)


list = [6, 5, 4, 3, 8, 2, 1, 7, 9, 0]
print(f'Unsorted List: {list}')
print(f'Sorted List:   {quick_sort(list)}')
