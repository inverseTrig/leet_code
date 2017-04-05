# Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
	    return 0
	
	index = 0
	
	for i in xrange(len(nums)):
	    if nums[i] != val:
		nums[index] = nums[i]
		index += 1
		
	return index
