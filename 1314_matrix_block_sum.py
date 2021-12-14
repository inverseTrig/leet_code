from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rangeSum[i + 1][j + 1] = rangeSum[i + 1][j] + \
                    rangeSum[i][j + 1] - rangeSum[i][j] + mat[i][j]
                print(rangeSum)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m, i + k + 1), min(n, j + k + 1)
                ans[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - \
                    rangeSum[r2][c1] + rangeSum[r1][c1]
        return ans


sol = Solution()
print(sol.matrixBlockSum(
    mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], k=1))
