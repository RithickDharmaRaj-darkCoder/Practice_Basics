# Selection Sort...

lst = []
lsize = int(input("\nEnter how many elements to be insert : "))
for i in range(lsize):
    elst = int(input("Enter the elements to add it in list : "))
    lst.append(elst)
print("Before Selection Sort : ", lst)

for outer in range(len(lst) - 1):
    min_index = outer
    for inner in range(outer + 1, len(lst)):
        if lst[min_index] > lst[inner]:
            min_index = inner
    if lst[outer] != lst[min_index]:
        lst[outer], lst[min_index] = lst[min_index], lst[outer]
print("After Selection Sort : ", lst)
