# Copy file...

# Collection of Alphabetic Numbers...

def a():  #23 Letter 'A' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if ((column == 0 or column == 4) and row != 0) or ((row == 0 or row == 3) and (column > 0 and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def b():  #24 Letter 'B' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (column == 4 and (row != 0 and row != 3 and row != 6)) or (
                        (row == 0 or row == 3 or row == 6) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def c():  #25 Letter 'C' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def d():  #26 Letter 'D' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 1) or (column == 4 and (row != 0 and row != 6)) or (
                        (row == 0 or row == 6) and (column != 4 and column != 6)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def e():  #27 Letter 'E' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or ((row == 0 or row == 3 or row == 6) and (0 < column)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def f():  #28 Letter 'F' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or ((row == 0 or row == 3) and (column > 0)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def g():  #29 Letter 'G' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (column == 4 and (row != 1 and row != 2 and row != 3)) or (
                        row == 0 and (0 < column and column < 4)) or (row == 4 and column != 1) or (
                        row == 5 and column == 2) or (row == 6 and (0 < column and column < 3)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def h():  #30 Letter 'H' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0 or column == 4) or (row == 3):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def i():  #31 Letter 'I' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 2) or (row == 0 or row == 6):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def j():  #32 Letter 'J' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 2) or (row == 0) or (row == 6 and column < 2) or (column == 0 and row == 5):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def k():  #33 Letter 'K' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        r = 0
        c = 4
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0):
                    print(f" {sq} ", end="")
                elif (row == column + 2 and column > 1):
                    print(f" {sq} ", end="")
                elif (row == r and column == c):
                    print(f" {sq} ", end="")
                    r += 1
                    c -= 1
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def l():  #34 Letter 'L' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (row == 6):
                    print(f" {sq} ",end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def m():  #35 Letter 'M' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(7):
                if (column == 0 or column == 6) or (row == 2 and (column == 2 or column == 4)):
                    print(f" {sq} ", end="")
                elif (row == 1 and (column < 2 or column >4)) or (row == 3 and column == 3):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def n():  #36 Letter 'N' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(7):
                if (column == 0 or column == 6):
                    print(f" {sq} ", end="")
                elif (row == column):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def o():  #37 Letter 'O' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if ((column == 0 or column == 4) and (row != 0 and row != 6)) or (
                        row == 6 and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                elif (row == 0 and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def p():  #38 Letter 'P' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or ((row == 0 or row == 3) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                elif (column == 4 and (row == 1 or row == 2)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def q():  #39 Letter 'Q' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(8):
            print("    ", end="")
            for column in range(6):
                if ((column == 0 or column == 4) and (row != 0 and row != 6 and row != 7)):
                    print(f" {sq} ", end="")
                elif ((row == 0 or row == 6) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                elif ((row == column + 2) and (column > 1)) or (column == 1 and row == 4):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def r():  #40 Letter 'R' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 0) or (column == 4 and (row == 1 or row == 2)):
                    print(f" {sq} ", end="")
                elif ((row == 0 or row == 3) and (0 < column and column < 4)):
                    print(f" {sq} ", end="")
                elif (row == column + 2) and (row > 3):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def s():  #41 Letter 'S' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (row == 0 or row == 3 or row == 6) and (column != 0 and column != 4):
                    print(f" {sq} ", end="")
                elif (column == 0 and 0 < row < 3):
                    print(f" {sq} ", end="")
                elif (column == 4 and 3 < row < 6):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def t():  #42 Letter 'T' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (row == 0):
                    print(f" {sq} ", end="")
                elif (column == 2):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def u():  #43 Letter 'U' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if ((column == 0 or column == 4) and row != 6):
                    print(f" {sq} ", end="")
                elif (row == 6 and (0 < column < 4)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def v():  #44 Letter 'V' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if ((column == 0 or column == 4) and (row != 6 and row != 5)):
                    print(f" {sq} ", end="")
                elif (row == 6 and column == 2):
                    print(f" {sq} ", end="")
                elif (row == 5 and (column == 1 or column == 3)):
                    print(f" {sq} ", end="")
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def w():  #45 Letter 'W' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
     for row in range(7):
         print("    ", end="")
         for column in range(5):
             if (column == 0 or column == 4) and (row != 0):
                 print(f" {sq} ", end="")
             elif (row == 4 and column == 2):
                 print(f" {sq} ", end="")
             elif (row == 5 and (column == 1 or column == 3)):
                 print(f" {sq} ", end="")
             else:
                 print(end="   ")
         print()
    else:
     print("Warning! Enter only '1' Character.")

def x():  #46 Letter 'X' ...
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

def y():  #47 Letter 'Y' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        r = 0
        c = 4
        for row in range(7):
            print("    ", end="")
            for column in range(5):
                if (column == 2 and row > 2):
                    print(f" {sq} ", end="")
                elif (row == column) and (row < 3):
                    print(f" {sq} ", end="")
                elif (row == r and column == c) and (row < 3):
                    print(f" {sq} ", end="")
                    r += 1
                    c -= 1
                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")

def z():  #48 Letter 'Z' ...
    sq = input("Enter one element : ").upper()
    if len(sq) == 1:
        r = 0
        c = 6
        for row in range(7):
            print("    ", end="")
            for column in range(7):
                if (row == r and column == c):
                    print(f" {sq} ", end="")
                    r += 1
                    c -= 1
                elif (row == 0 or row == 6):
                    print(f" {sq} ", end="")

                else:
                    print(end="   ")
            print()
    else:
        print("Warning! Enter only '1' Character.")
