# 4Sum

class Solution(object):
    def fourSum(self, nums, target):
        res = []
	length = len(nums)
	
	if (nums == [] or len < 4):
	    return res
	
	nums.sort()
	
	maximum = nums[length - 1]
	
	if 4 * nums[0] > target or 4 * maximum < target:
	    return res
	    
	for i in xrange(length):
	    z = nums[i]
	    if i > 0 and z == nums[i-1]:
		continue
	    if (z + 3 * maximum < target):
		continue
	    if 4 * z > target:
		break
	    if 4 * z == target:
		if (i + 3 < length and nums[i+3] == z):
		    res.append([z, z, z, z])
		break
	    
	    Solution().threeSumForFourSum(nums, target - z, i + 1, length - 1, res, z)
	
	return res
	
    
    def threeSumForFourSum(self, nums, target, low, high, fourSumList, z1):
	if low + 1 >= high:
	    return
	
	maximum = nums[high]
	if 3 * nums[low] > target or 3 * maximum < target:
	    return
	
	for i in xrange(low,high-1):
	    z = nums[i]
	    if i > low and z == nums[i - 1]:
		continue
	    if z + 2 * maximum < target:
		continue
	    if 3 * z > target:
		break
	    if 3 * z == target:
		if i + 1 < high and nums[i + 2] == z:
		    fourSumList.append([z1, z, z, z])
		break
	    
	    Solution().twoSumForFourSum(nums, target - z, i + 1, high, fourSumList, z1, z)
    
	
	
    def twoSumForFourSum(self, nums, target, low, high, fourSumList, z1, z2):
	if low >= high:
	    return
	
	if 2 * nums[low] > target or 2 * nums[high] < target:
	    return
	    
	i, j = low, high
	
	while i < j:
	    add = nums[i] + nums[j]
	    if add == target:
		fourSumList.append([ z1, z2, nums[i], nums[j] ])
		
		i += 1
		while i < j and nums[i] == nums[i-1]:
		    i += 1
		    
		j -= 1
		while i < j and nums[j] == nums[j+1]:
		    j -= 1
		    
	    if add < target:
		i += 1
		
	    if add > target:
		j -= 1
