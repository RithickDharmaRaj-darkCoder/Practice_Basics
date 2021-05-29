# practice section...

sq = input("Enter one element : ").upper()
for row in range(7):
    print("    ", end="")
    for column in range(5):
        if (column == 2) or (row == 0 or row == 6):
            print(f" █ ",end="")
        else:
            print(end="   ")
    print()
