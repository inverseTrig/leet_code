from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                left_min = right_min = matrix[row - 1][col]
                if col > 0:
                    left_min = min(matrix[row - 1][col - 1], left_min)
                if col < len(matrix[0]) - 1:
                    right_min = min(matrix[row - 1][col + 1], right_min)

                matrix[row][col] += min(right_min, left_min)

        return min(matrix[-1])


sol = Solution()
print(sol.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(sol.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]))
