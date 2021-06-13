# Merge Sort...

lsize = int(input('How many numbers want to insert : '))
lst = [int(input(f'Add Number {i+1} : '))for i in range(lsize)]
print(f'Before Merge Sort : {lst}')
def merging2list(lft,right):
    result = []
    i,j = 0,0
    while i < len(lft) and j < len(right):
        if lft[i] < right[j]:
            result.append(lft[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += lft[i:]
    result += right[j:]
    return result

def divide(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid_val = len(lst) // 2
        lft = divide(lst[:mid_val])
        right = divide(lst[mid_val:])
        return merging2list(lft,right)

print(f'After Merge Sort : {divide(lst)}')