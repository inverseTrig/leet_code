from typing import List
from itertools import accumulate


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        values = [0] + list(accumulate(nums))
        max_val = float('-inf')
        for i in range(0, len(nums) - k + 1):
            max_val = max(values[i + k] - values[i], max_val)
        return max_val / k


sol = Solution()
print(sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(sol.findMaxAverage(nums=[5], k=1))
