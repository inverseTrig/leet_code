# Subsets

class Solution(object):
	def subsets(self, num):
		res = [[]]
		for num in sorted(nums):
			res += [[item+[num] for item in res]
		return res
		
