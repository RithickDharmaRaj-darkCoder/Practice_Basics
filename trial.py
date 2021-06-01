# String Methods...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    # r = int(input("Enter no.of rows : "))
    c = 1
    for row in range(5):
        print("    ", end="")
        for space in range(5 - row - 1):
            print(end="   ")
        for column in range(2*row+1):
            print(sq , end="  ")
        print()
else:
    print("Warning! Enter only '1' Character.")