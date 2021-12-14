from typing import List


class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] += dp[target - coin]
                print(dp)
        return dp[amount]


sol = Solution()
print(sol.change(amount=5, coins=[1, 2, 5]))
