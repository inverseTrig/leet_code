# Jump Game

class Solution(object):
	def canJump(self, nums):
		if (len(nums) < 2):
			return True
			
		for i in range(len(nums)-2, -1, -1):
			if nums[i] == 0:
				jumpsRequired = 1
				while jumpsRequired > nums[i]:
					jumpsRequired += 1
					i -= 1
					if i < 0:
						return False
		return True
