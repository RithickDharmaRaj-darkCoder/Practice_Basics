# Range Datatype ...

for row in range(5):
    print("     ", end=" ")
    for column in range(row + 1):
        print('*', end=" ")
    print()