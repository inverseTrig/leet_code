from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                prev_min = min(grid[i - 1][:j] + grid[i - 1][j + 1:])
                grid[i][j] += prev_min

        return min(grid[-1])


sol = Solution()
print(sol.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.minFallingPathSum(grid=[[7]]))
