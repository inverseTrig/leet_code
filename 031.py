# Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        if nums != []:
	    z = len(nums) - 1
	    index = -1
	    for i in range(z,0,-1):
		if nums[i-1] < nums[i]: #
		    index = i - 1
		    
		    for j in range(z, index, -1):
			if nums[j] > nums[index]:
			    Solution().swap(nums, index, j)
			    Solution().reverseSort(nums, index + 1, z)
			    return
	    if index == -1:
		Solution().reverseSort(nums, 0, z)
	
	return
		    
		
    def swap(self, nums, index, j):
	nums[index] += nums[j]
	nums[j] = nums[index] - nums[j]
	nums[index] -= nums[j]
	return nums
	
    def reverseSort(self, nums, start, end):
	if start < end:
	    for i in range(start,(start + end + 1)/2):
		Solution().swap(nums, i, start + end - i)
	return nums
	    


