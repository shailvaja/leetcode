def twoSum(nums, target: int) :
    map = {}
    for x in range(len(nums)):
        map[nums[x]] = x
    for x in range(len(nums)):
        y = target - nums[x]
        if y in map and map[y]!=x:
            return [x,map[y]]

print(twoSum([2,7,11,15], 9))