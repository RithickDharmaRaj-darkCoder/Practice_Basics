# Heap Sort...

def heapify(lst,n,p_index):
    largest = p_index
    left_child_index = p_index * 2 + 1
    right_child_index = p_index * 2 + 2

    if left_child_index < n and lst[largest] < lst[left_child_index]:
        largest = left_child_index
    if right_child_index < n and lst[largest] < lst[right_child_index]:
        largest = right_child_index
    if largest != p_index:
        lst[p_index],lst[largest] = lst[largest],lst[p_index]
        heapify(lst,n,largest)

def heapsort(lst):
    for p_index in range(n // 2 -1,-1,-1):
        heapify(lst,n,p_index)
    for len in range(n-1,0,-1):
        lst[len],lst[0] = lst[0],lst[len]
        heapify(lst,len,0)

lsize = int(input('How many numbers want to insert : '))
lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
print(f'Before Heap Sort : {lst}')
n = len(lst)
heapsort(lst)
print(f'After Heap Sort : {lst}')