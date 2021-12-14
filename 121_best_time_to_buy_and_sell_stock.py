from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_max = prices[-1]
        profit = 0
        for i in range(len(prices) - 1, -1, -1):
            prev_max = max(prev_max, prices[i])
            profit = max(profit, prev_max - prices[i])
        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
