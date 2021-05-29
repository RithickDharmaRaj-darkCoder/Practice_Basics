# practice section...

sq = input("Enter one element : ").upper()
for row in range(7):
    print("    ", end="")
    for column in range(5):
        if (column == 0 ) or (column == 4 and  ( row != 1 and row != 2 and row != 3)) or (row == 0 and (0 < column and column < 4 )) or (row == 4 and column != 1) or (row ==5 and column == 2) or (row == 6 and (0 < column and column < 3)):
            print(f" {sq} ",end="")
        else:
            print(end="   ")
    print()
