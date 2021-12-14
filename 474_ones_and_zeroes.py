from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            dm = s.count("0")
            dn = len(s) - dm
            for M in range(m, dm - 1, -1):
                for N in range(n, dn - 1, -1):
                    dp[M][N] = max(dp[M - dm][N - dn] + 1, dp[M][N])
        return dp[-1][-1]


sol = Solution()
print(sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
