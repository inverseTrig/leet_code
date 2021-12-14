from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dp = [[None] * N for _ in range(N)]

        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                if (xj - xi) == 0:
                    continue
                slope = (yj - yi) / (xj - xi)
                incpt = yj - (slope * xj)
                dp[i][j] = (slope, incpt)
        print(dp)


sol = Solution()
print(sol.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
