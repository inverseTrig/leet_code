class Solution:
    def maxSum(self, nums: List[int]) -> int:
        minimum = min(0, max(nums))
        unique_numbers = {i for i in nums if i >= minimum or i > 0}
        return sum(unique_numbers)

