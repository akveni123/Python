def count(list):
    even = 0
    odd = 0
    for i in list:
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    return even, odd

number_of_elem = int(input('Enter number of elems : '))
list = []
for i in range(number_of_elem):
    num = int(input())
    list.append(num)


even ,odd = count(list)
print('even : {}, ood: {}'.format(even,odd))
# print('number of odd: ', odd)