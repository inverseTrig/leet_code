from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid_point = (left + right)//2
                if target > nums[mid_point]: left = mid_point + 1
                else: right = mid_point - 1
            return left

        def findRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid_point = (left + right)//2
                if target >= nums[mid_point]: left = mid_point + 1
                else: right = mid_point - 1
            return right

        left, right = findLeft(nums, target), findRight(nums, target)
        return [left, right] if left <= right else [-1, -1]


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
