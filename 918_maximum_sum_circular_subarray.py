from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        cur_max, cur_min = 0, 0
        max_sum, min_sum = 0, 0

        for i in range(0, len(nums)):
            cur_max = max(nums[i], nums[i] + cur_max)
            max_sum = max(cur_max, max_sum)

            cur_min = min(nums[i], nums[i] + cur_min)
            min_sum = min(cur_min, min_sum)

        return max(max_sum, sum(nums) - min_sum)


sol = Solution()
print(sol.maxSubarraySumCircular([5,-3,5]))
