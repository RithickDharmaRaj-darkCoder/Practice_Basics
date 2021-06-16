# ...

name = 'ABBAAB'
lett_A = [[' ' for i in range(7)] for j in range(7)]
lett_B = [[' ' for i in range(7)] for j in range(7)]

for row in range(7):
    for column in range(5):
        if ((column == 0 or column == 4) and row != 0) or ((row == 0 or row == 3) and (column > 0 and column < 4)):
            lett_A[row][column] = '%'

for row in range(7):
    for column in range(5):
        if (column == 0) or (column == 4 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (0 < column and column < 4)):
            lett_B[row][column] = '%'

for i in range(7):
    for j in range(5):
        print(lett_A[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(lett_B[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(lett_A[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(lett_B[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(lett_A[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(lett_B[i][j],end=" ")
    print(end=" ")
    print()
