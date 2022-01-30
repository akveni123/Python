
def selectionsort(nums):
    for i in range(len(nums)-1):
        midpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[midpos]:
                midpos = j

        temp = nums[i]
        nums[i] = nums[midpos]
        nums[midpos] = temp

        # /print(nums)

nums = [70,8,5,100,5,6,34,90,]

selectionsort(nums)
print(nums)