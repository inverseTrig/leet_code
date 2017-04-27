# Combination Sum

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combi = []
	candidates.sort()
	self.dfs(candidates, target, 0, [], combi)
	return combi
	
    def dfs(self, nums, target, index, path, combi):
	if target < 0:
	    return
	if target == 0:
	    combi.append(path)
	    return
	for i in xrange(index, len(nums)):
	    self.dfs(nums, target - nums[i], i, path+[nums[i]], combi)
