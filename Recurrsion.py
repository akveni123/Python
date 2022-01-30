import sys
# print(sys.getrecursionlimit())

# sys.setrecursionlimit(10)

def greet():
    print('Hello')
    greet()
# fun calling
# greet()

# max recurssion is 1000 but can be modified

# factorial using recurrsion
def fact(n):
    if(n==0):
        return 1
    
    return n*fact(n-1)

x = int(input('Enter value: '))

result = fact(x)
print('factorial of {} is : {}'.format(x,result))