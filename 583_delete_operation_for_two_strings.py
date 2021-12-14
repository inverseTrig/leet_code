class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1), len(word2)

        dp = [[0] * (w2_len + 1) for _ in range(w1_len + 1)]
        for i, w1c in enumerate(word1):
            for j, w2c in enumerate(word2):
                if w1c == w2c:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return w1_len + w2_len - 2 * dp[-1][-1]


sol = Solution()
print(sol.minDistance(word1="sea", word2="eat"))
print(sol.minDistance(word1="leetcode", word2="etco"))
