from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        width = len(nums) + 1
        for right in range(len(nums)):
            target -= nums[right]
            while target <= 0:
                width = min(width, right - left + 1)
                target += nums[left]
                left += 1
        return width % (len(nums) + 1)


sol = Solution()
print(sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(sol.minSubArrayLen(target=15, nums=[1, 2, 3, 4, 5]))
