from numpy import *

arr = array([1,2,3,4,5])

arr1 = array([0,0,0,0,0])

arr2 = concatenate([arr,arr1])

print(arr2)

arr3 = arr.copy()
print(arr)
print(arr3)

if id(arr) == id(arr3):
    print('True')
    print(id(arr))
else:
    print('False')