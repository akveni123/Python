def sort(list):
    for i in range((len(list)-1),0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [4,3,6,5,4,8,90]
sort(list)
print(len(list))
print(list)