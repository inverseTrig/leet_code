from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        result = str_nums[0]
        if len(nums) == 2:
            result += "/" + str_nums[1]
        elif len(nums) > 2:
            result += "/" + "(" + "/".join(str_nums[1:]) + ")"
        return result


sol = Solution()
print(sol.optimalDivision(nums=[1000, 100, 10, 2]))
print(sol.optimalDivision(nums=[2, 3, 4]))
print(sol.optimalDivision(nums=[2]))
print(sol.optimalDivision(nums=[2, 3]))
