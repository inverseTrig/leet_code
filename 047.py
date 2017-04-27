# Permutations II

import itertools

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(itertools.permutations(nums)))

print(Solution().permute([1, 1, 2]))
