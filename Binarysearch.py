#Binary Search 
nums = [12,34,2,56,90,33,89,120,20,25,19]
nums = sorted(nums)

target = 34 
#target = 97

left = 0 
right  = len(nums) - 1
found = False

while left<=right:
    mid = (left+right)//2
    if nums[mid] == target:
        found = True
        break
    elif mid[nums] > target :
        right = mid -1
    else:
        left = mid +1
    

if found==True : 
    print("Element is present in list")
else:
    print("Element is not present")
