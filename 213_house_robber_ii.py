from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.choice(nums[1:]), self.choice(nums[:-1]))

    def choice(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            a, b = b, max(a + num, b)
        return b
