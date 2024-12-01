def findMin(nums):
    res = num[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]: # if array is already in ascending order
            res = min(res, nums[l])
            break
        
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]: # if middle is larger then l, search right side of sorted array
            l = m + 1
        else: # if middle is less then left, then search left side of sorted array
            r = m - 1
    return res