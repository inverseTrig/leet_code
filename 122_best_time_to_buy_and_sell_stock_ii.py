from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last_max = 0
        for i in range(len(prices) - 1, -1, -1):
            last_max = max(last_max, prices[i])
            if prices[i] < last_max:
                profit += last_max - prices[i]
                last_max = prices[i]
        return profit
