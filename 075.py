# Sort Colors

class Solution(object):
	def sortColors(self, nums):
		i = 0
		j = 0
		for k in range(0,len(nums)):
			temp = nums[k]
			nums[k] = 2
			if temp < 2:
				nums[j] = 1
				j += 1
			if temp == 0:
				nums[i] = 0
				i += 1
