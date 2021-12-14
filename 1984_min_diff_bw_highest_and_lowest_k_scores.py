from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        minimum = min([abs(nums[i + k - 1] - nums[i])
                       for i in range(0, len(nums) - k + 1)])
        return minimum


sol = Solution()
print(sol.minimumDifference(nums=[9, 4, 1, 7], k=2))
