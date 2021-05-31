# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    r = 0
    c = 4
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (row == r and column == c):
                print(f" {sq} ", end="")
                r = r + 1
                c = c - 1
            elif (row == column):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
