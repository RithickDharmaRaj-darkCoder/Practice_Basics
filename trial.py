# String Methods...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    print()
    # r = int(input("Enter no.of rows : "))
    c = 0
    s = 9
    for row in range(s):
        print("    ", end="")
        for space in range(9 - s):
            print(end="  ")
        for column in range(9-c):
            print(sq+" ", end="  ")
        c += 2
        s -= 2
        print()
else:
    print("Warning! Enter only '1' Character.")