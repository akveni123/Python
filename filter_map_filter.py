from functools import reduce

# get even number from a list

def evenNos(n):
    if n%2 ==0:
        return n 

num = [2,5,7,8,4,22,4]
# lst = list(filter(evenNos,num))

# how to use lamba

evenlst = list(filter(lambda n: n%2==0,num))

lst1 = evenlst

# print('Even numbers: {}'.format(lst1))

# map
multiply = list(map(lambda a : a*2, evenlst))

# print(multiply)

print('Multiply: {}'.format(multiply))

#add using reduce cocept

addeelist = reduce(lambda a,b: a+b, multiply)

print('Addition: {}'.format(addeelist))

