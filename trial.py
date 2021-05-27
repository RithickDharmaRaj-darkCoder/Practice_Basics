# practice section...

sq = input("Enter one element : ").upper()
# r = int(input("Enter no.of rows : "))
for row in range(6):
    print("     ", end=" ")
    for column in range(row+1):
        print(sq,end=" ")
    print()
for row in range(5):
    print("     ", end=" ")
    for column in range(5 - row, 0, -1):
        print(sq + "", end=" ")
    print()