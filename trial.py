# practice section...

sq = input("Enter one element : ").upper()
for row in range(7):
    print("    ", end="")
    for column in range(5):
        if (column == 0 or column == 4) or (row == 3):
            print(f" {sq} ",end="")
        else:
            print(end="   ")
    print()
