def fact(n):
    f =1
    for i in range(1,n+1):
        f = f*i
    return f

x = int(input('Enter a number: '))

factorial = fact(x)

print('factorial of {} is {}'.format(x,factorial))