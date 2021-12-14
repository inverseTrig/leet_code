from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = result = nums[0]
        for num in nums[1:]:
            min_product, max_product = min(num, num * max_product, num * min_product), max(num, num * max_product, num * min_product)
            result = max(max_product, result)
        return result


sol = Solution()
print(sol.maxProduct(nums = [2,3,-2,4]))
