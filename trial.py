# Numerical Patterns ...


k = 0
for row in range(4):
    print("    ",end=" ")
    for space in range(4-row-1):
        print(" ",end=" ")
    for column in range(row+1):
        print(k,end=" ")
        k += 1
    print()
