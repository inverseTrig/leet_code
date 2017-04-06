# Search for a Range

class Solution(object):
    def searchRange(self, nums, target):
        if nums == [] or target is None:
	    return [-1, -1]
	else:
	    n = len(nums) - 1
	    index = Solution().bisectSearch(nums, target, 0, n)
	    if index == None:
		return [-1, -1]
	    else:
		i, j = index, index
		while i > 0 and nums[i] == nums[i-1]:
		    i -= 1
		while j < n and nums[j] == nums[j+1]:
		    j += 1
	
	return [i, j]
	    
	    
    def bisectSearch(self, nums, target, i, j):
	if target in nums:
	    if nums[(j+i)//2] < target:
		return Solution().bisectSearch(nums, target, (j+i)//2 + 1, j)
	    elif nums[(j+i)//2] > target:
		return Solution().bisectSearch(nums, target, i, (j+i)//2 - 1)
	    else:
		return (j+i)//2
	else:
	    return None
