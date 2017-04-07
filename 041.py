# First Missing Positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
	    while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
		Solution().swap(nums, i, nums[i] - 1)
		
	for j in range(0, len(nums)):
	    if nums[j] != j + 1:
		return j + 1
	
	return len(nums) + 1
	
    
    def swap(self, nums, i, j):
	nums[i] += nums[j]
	nums[j] = nums[i] - nums[j]
	nums[i] -= nums[j]

print(Solution().firstMissingPositive([0]))
