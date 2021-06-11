# Bubble Sort...

size = int(input("How many numbers want to insert : "))
lst1 = []
for iput in range(size):
    lst2 = int(input("Enter the number : "))
    lst1.append(lst2)

print(f'\nOriginal lst : {lst1}\n')
for repeat in range(len(lst1)-1):
    for num in range(len(lst1)-1):
        if lst1[num] > lst1[num + 1]:
            lst1[num],lst1[num + 1] = lst1[num + 1],lst1[num]
    print(f'Iteration {repeat+1} : {lst1}')

print(f'\nBubble Sort :{lst1}')
