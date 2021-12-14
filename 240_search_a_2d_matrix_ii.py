from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(i: int = 0, j: int = len(matrix[0]) - 1):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return False

            if matrix[i][j] == target:
                return True

            return search(i + 1, j) \
                if target > matrix[i][j] \
                else search(i, j - 1)

        return search()


sol = Solution()
print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
                       20))
