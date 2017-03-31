class Solution:
    def twoSum(self, nums, target):
    	for i, x in enumerate(nums):
		    if i == len(nums):
    			break
			    
		    for j in range (i+1, len(nums)):
			    y = nums[j]
    			
			    if x + y == target:
    				return i, j
    	return None
				
