from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        max_val = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i][j],
                                           dp[i + 1][j],
                                           dp[i][j + 1]
                                           ) + 1
                max_val = max(max_val, dp[i + 1][j + 1])

        return max_val ** 2


sol = Solution()
print(sol.maximalSquare(matrix=[["1", "0", "1", "0", "0"], [
      "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
