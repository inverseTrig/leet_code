# Single Number

class Solution(object):
	def singleNumber(self, nums):
		val = 0
		for i in nums:
			val ^= i
		return val
