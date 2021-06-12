# Merge Sort...

def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        lft_lst = lst[:mid]
        right_lst = lst[mid:]
        mergesort(lft_lst)
        mergesort(right_lst)

        (i,j,k) = (0,0,0)
        while len(lft_lst) > i and len(right_lst) > j:
            if lft_lst[i] < right_lst[j]:
                lst[k] = lft_lst[i]
                i += 1
                k += 1
            else:
                lst[k] = right_lst[j]
                j += 1
                k += 1

        while len(lft_lst) > i:
            lst[k] = lft_lst[i]
            i += 1
            k += 1
        while len(right_lst) > j:
            lst[k] = right_lst[j]
            j += 1
            k += 1
lsize = int(input('How many numbers want to add : '))
lst = [int(input(f'Add number {i+1} : '))for i in range(lsize)]
print(f'Before Merge Sort : {lst}')
mergesort(lst)
print(f'After Merge Sort : {lst}')
