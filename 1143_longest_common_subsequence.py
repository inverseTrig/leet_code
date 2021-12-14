class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                if t1 == t2:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]


sol = Solution()
print(sol.longestCommonSubsequence(text1="abcde", text2="ace"))
print(sol.longestCommonSubsequence(text1="abc", text2="abc"))
print(sol.longestCommonSubsequence(text1="abc", text2="def"))
