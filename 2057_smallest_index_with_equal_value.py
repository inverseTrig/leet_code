from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1


sol = Solution()
print(sol.smallestEqual(nums=[2, 1, 3, 5, 2]))
print(sol.smallestEqual(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(sol.smallestEqual(nums=[4, 3, 2, 1]))
