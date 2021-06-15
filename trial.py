# Quick Sort...

lsize = int(input('How many numbers want to insert : '))
lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
print(f'Before Quick Sort : {lst}')

def quick(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        key = lst.pop()

    lower_elements = []
    greater_elements = []

    for element in lst:
        if element < key:
            lower_elements.append(element)
        else:
            greater_elements.append(element)

    return quick(lower_elements) + [key] + quick(greater_elements)

print(f'After Quick Sort  : {quick(lst)}')