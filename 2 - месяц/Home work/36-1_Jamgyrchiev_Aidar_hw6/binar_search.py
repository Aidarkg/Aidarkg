def binary_search(item, lists):
    global middle
    first = 0
    last = len(lists) - 1
    resultok = False

    while first <= last:
        middle = (first + last) // 2
        if lists[middle] == item:
            resultok = True
            break
        elif lists[middle] < item:
            first = middle + 1
        else:
            last = middle - 1

    if resultok:
        return middle
    else:
        return - 1


n = list(range(1, 5001))
binary = binary_search(200, n)
if binary != -1:
    print(f'Index element: {binary}')
else:
    print('No element')

