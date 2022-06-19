def fix_calendar(nums):
    for i in range(len(nums)):
        for r in range(len(nums)):
            if nums[i] < nums[r]:
                nums[i], nums[r] = nums[r], nums[i]
    return nums


