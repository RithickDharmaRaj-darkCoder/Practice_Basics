# Insertion Sort...


lsize = int(input("\nEnter how many elements to be insert : "))
lst = [int(input(f'Add element {i+1} : ')) for i in range(lsize)]
print(f'Before Insertion Sort : {lst}')


for index in range(1,len(lst)):
    curent_value = lst[index]
    postion = index
    while (curent_value < lst[postion-1] ) and (postion > 0):
        lst[postion] = lst[postion-1]
        postion -= 1
    lst[postion] = curent_value
print(f'After Insertion Sort : {lst}')