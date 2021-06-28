def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Or the following works:

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False