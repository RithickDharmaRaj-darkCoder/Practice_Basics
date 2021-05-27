# practice section...

sq = input("Enter one element : ").upper()
# r = int(input("Enter no.of rows : "))
for row in range(5):
    print("    ", end="")
    for space in range(row):
        print(" ", end=" ")
    for column in range(5-row):
        print(sq+"  ", end=" ")
    print()
