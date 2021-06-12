# Insertion Sort...

lst = []
lsize = int(input("\nEnter how many elements to be insert : "))
for i in range(lsize):
    elst = int(input(f"Add Element {i+1} : "))
    lst.append(elst)
print(f'Before Insertion Sort : {lst}')

for index in range(1,len(lst)):
    curent_value = lst[index]
    postion = index
    while (curent_value < lst[postion-1] ) and (postion > 0):
        lst[postion] = lst[postion-1]
        postion -= 1
    lst[postion] = curent_value
print(f'After Insertion Sort : {lst}')