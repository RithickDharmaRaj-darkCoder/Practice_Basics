# 11'O Clock Study ...

# 1. Write a python program to do multiplication & division
# by getting inputs from the user.def disply():

# 1. Get input in numbers ...
# 2. Do fibanocci and print each numbers ...
# 3. And also do Factorial of that number in ascending order ...
# 4. Print the sum of the fibo... and fact...

iput = int(input('Enter one number : '))

# Fibonacci Section [0,1,1,2,3,5,8,13,...] ...
fib_lst = []
if iput == 0:
    pass
elif iput == 1:
    fib_lst.append(0)
else:
    fib_lst.append(0)
    fib_lst.append(1)
    a = 0
    b = 1
    for num in range(iput-2):
        c = a + b
        fib_lst.append(c)
        a = b
        b = c
print(f'\nFibanocci      : {fib_lst}')

# Factorial Section [1,2,6,24,120,720,...] ...
fact_lst = []
if iput == 0:
    pass
elif iput == 1:
    fact_lst.append(1)
else:
    fact_lst.append(1)
    a = 1
    for num in range(2,iput+1):
        c = a * num
        fact_lst.append(c)
        a = c
print(f'Factorial      : {fact_lst}')

# Final Section Fib[] + Fact[] ...
result = []
for num in range(len(fib_lst)):
    result.append(fib_lst[num]+fact_lst[num])
print(f'\nSum(Fib+Fact)  : {result}')
