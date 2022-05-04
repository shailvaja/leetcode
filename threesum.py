def threeSum(nums):
        output = []
        temp_output = []
        for x in range(len(nums)):
            for y in range(x, len(nums)):
                if x !=y:
                    z = 0-(nums[x] + nums[y])
                    if z in nums:
                        ind = nums.index(z)
                        if  ind!=x and ind!=y:
                            temp_output.append(nums[x])
                            temp_output.append(nums[y])
                            temp_output.append(z)
                            temp_output.sort()
                            if temp_output not in output:
                                output.append(temp_output)
                            temp_output = []
                    
        return output  

def threeSum_recurse(nums):
    output = []
    
    h_map = {}
    for x in range(len(nums)):
        h_map[x] = nums[x]

    def recurse(x, y, lst):
        if len(lst) == 0:
            return
       
        if nums[x] + nums[y] + lst[0] == 0:
                temp_output = [nums[x], lst[0], nums[y]]
                temp_output.sort()
                if temp_output not in output:
                    output.append(temp_output)
                temp_output = []    
        recurse(x, y, lst[1:]) 
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):

            recurse(x, y, nums[y+1:])       
    return output

print(threeSum_recurse([-1,0,1,2,-1,-4]))