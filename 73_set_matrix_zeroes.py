from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        I, J = len(matrix), len(matrix[0])
        zeroes = []
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    zeroes.append((i, j))

        for i, j in zeroes:
            for _i in range(0, I):
                matrix[_i][j] = 0
            for _j in range(0, J):
                matrix[i][_j] = 0
        print(matrix)


sol = Solution()
print(sol.setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(sol.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
