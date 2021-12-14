from typing import List


class Solution:
    def maxSumRangeQuery(self,
                         nums: List[int],
                         requests: List[List[int]]) -> int:
        dp = [0] * (len(nums) + 1)
        for s, e in requests:
            dp[s] += 1
            dp[e + 1] -= 1

        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        dp = [each for each in dp if each]
        dp.sort(reverse=True)
        nums.sort(reverse=True)

        result = 0
        for x, y in zip(dp, nums):
            result += x * y
        return result


sol = Solution()
print(sol.maxSumRangeQuery(nums=[1, 2, 3, 4, 5], requests=[[1, 3], [0, 1]]))
print(sol.maxSumRangeQuery(nums=[1, 2, 3, 4, 5, 6], requests=[[0, 1]]))
print(sol.maxSumRangeQuery(
    nums=[1, 2, 3, 4, 5, 10], requests=[[0, 2], [1, 3], [1, 1]]))
