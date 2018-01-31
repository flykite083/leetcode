def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    new_set = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                new_set.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

    new_set.sort()
    return [new_set[i] for i in range(len(new_set)) if i == 0 or new_set[i] != new_set[i - 1]]
print(threeSum([-1, 0, 1, 2, -1, -4]))
