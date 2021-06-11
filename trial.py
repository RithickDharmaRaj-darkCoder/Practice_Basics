# Selection Sort...

lst = []
lsize = int(input("Enter how many numbers want to add : "))
i = 1
for call in range(lsize):
    iput = int(input(f'Enter the number {i} : '))
    lst.append(iput)
    i += 1
print(f'Before Selection Sort : {lst}')

for outer in range(len(lst)):
    min_index = outer
    for inner in range(outer+1,len(lst)):
        if lst[min_index] > lst[inner]:
            min_index = inner
    if lst[outer] != lst[min_index]:
        lst[min_index],lst[outer] = lst[outer],lst[min_index]
    print(f'it{outer} : {lst}')
print(f'After Selection Sort : {lst}')