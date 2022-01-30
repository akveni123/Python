pos = -1
def linearSearch(list, n):
    i = 0
    for i in list:
        if list[i] == n:
            globals()['pos'] = i
            return True
        # i = i+1

    return False

# list = [33,24,5,96,77,30,12]
# n =24
# linear search
# found = linearSearch(list,n)

def BinarySearch(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    else:
        return False

list = [24,56,77,700,1092]
n =707
found = BinarySearch(list,n)
if found==True:
    print("value found at {}".format(pos))
else:
    print("not found")