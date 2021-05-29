# practice section...

sq = input("Enter one element : ").upper()
for row in range(7):
    print("    ", end="")
    for column in range(5):
        if (column == 1) or (column == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (column != 4 and column != 6) ):
            print(f" {sq} ",end="")
        else:
            print(end="   ")
    print()
