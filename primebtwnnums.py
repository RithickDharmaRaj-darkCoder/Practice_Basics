# Printing Prime Numbers...
print("    *** Prime Numbers between specific numbers ***")
def prime():
    try:
            start,end = input("Enter the starting and ending numbers : ").split()
            print(f"The Prime Numbers from {start} to {end} are : ")
            prime = []

            for numbers in range(int(start),int(end) + 1):
                if numbers == 2 or numbers == 3 or numbers == 5 or numbers == 7 or numbers == 11:
                    prime.append(numbers)
                elif numbers % numbers == 0 and numbers % 2 != 0 and numbers % 3 != 0 and numbers % 5 != 0 and numbers % 7 != 0 and numbers % 11 != 0 :
                    if numbers == 1:
                        continue
                    prime.append(numbers)
            for num in prime:
                print(num)
            if bool(prime) == False:
                print(f"     Oops! There is no prime numbers between {start} to {end}. ")
    except:
        print("Warning!   * Enter only 2 numbers by giving space between them * ")
        prime()
prime()

#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")
