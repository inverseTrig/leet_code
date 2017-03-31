class Solution:
    def twoSum(self, nums, target):
    	for i, x in enumerate(nums):
		    print ("Printing i, x: ", i, x)
    		
		    if i == len(nums):
    			break
			    
		    for j in range (i+1, len(nums)):
			    y = nums[j]
			    print("Printing j, y: ", j, y)
    			
			    if x + y == target:
    				return i, j
    	return None
				
