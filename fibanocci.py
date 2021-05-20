#Printing Fibanocci sequence for wanted order...
print("     *** Finiding Fibanocci Sequence *** \n")

def fibi():
    try:
        fib = int(input("Enter the Fibonacci order : F"))
        a,b,d = 0,1,2

        if fib == 0:
            print(f"F0 : {a}")
        else:
            print(f"F0 : {a}")
            print(f"F1 : {b}")

            for num in range(2,fib+1):
                c = a + b
                a = b
                b = c
                print(f"F{d} : {c}")
                d += 1
    except ValueError:
        print("Warning!, * Enter only the numbers *")
        fibi()
fibi()

#Personal Greetings...
print("Thank You!","\n","          -darkCoder \U0001F43E")