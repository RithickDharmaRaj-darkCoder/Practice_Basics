# String Methods...

# sq = int(input("How many rows needed? : "))
c = 1
for row in range(5):
    print("     ", end=" ")
    for column in range(1,c+1):
        print('*',end=" ")
    c += 2
    print()