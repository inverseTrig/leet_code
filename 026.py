# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
	if not nums:
	    return 0
	
	index = 0
	
	for i in xrange(len(nums)):
	    if nums[i] != nums[index]:
		index += 1
		nums[index] = nums[i]
		
	return index + 1
