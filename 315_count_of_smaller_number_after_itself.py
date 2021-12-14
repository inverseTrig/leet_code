from typing import List
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, seen = [], SortedList([])
        for i in range(len(nums) - 1, -1, -1):
            idx = seen.bisect_left(nums[i])
            seen.add(nums[i])
            res.insert(0, idx)
        return res


sol = Solution()
print(sol.countSmaller(nums=[5, 2, 6, 1]))
print(sol.countSmaller(nums=[-1]))
print(sol.countSmaller(nums=[-1, -1]))
