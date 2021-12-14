class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1] * (len(s) + 1)]
        dp.extend([[0] * (len(s) + 1) for _ in range(len(t))])
        for i, x in enumerate(t):
            for j, y in enumerate(s):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

        return dp[-1][-1]


sol = Solution()
print(sol.numDistinct(s="rabbbit", t="rabbit"))
print(sol.numDistinct(s="babgbag", t="bag"))
