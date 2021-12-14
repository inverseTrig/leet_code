from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        up, down = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)


sol = Solution()
print(sol.wiggleMaxLength(nums=[1, 7, 4, 9, 2, 5]))
print(sol.wiggleMaxLength(nums=[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
print(sol.wiggleMaxLength(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sol.wiggleMaxLength(nums=[3, 3, 3, 2, 5]))
print(sol.wiggleMaxLength(nums=[0, 0]))
