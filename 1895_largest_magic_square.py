from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        def isMagicSquare(size: int, i: int, j: int) -> bool:
            summation = set()

            for x in range(size):
                s = 0
                for y in range(size):
                    s += grid[i + x][j + y]
                summation.add(s)
                if len(summation) > 1:
                    return False

            for y in range(size):
                s = 0
                for x in range(size):
                    s += grid[i + x][j + y]
                summation.add(s)
                if len(summation) > 1:
                    return False

            f_diag = 0
            for x in range(size):
                f_diag += grid[i + x][j + x]
            summation.add(f_diag)
            if len(summation) > 1:
                return False

            b_diag = 0
            for x in range(size):
                b_diag += grid[i + x][j + (size - 1) - x]
            summation.add(b_diag)
            if len(summation) > 1:
                return False

            return True

        k = min(len(grid), len(grid[0]))
        for size in range(k, 1, -1):
            for i in range(len(grid) - size + 1):
                for j in range(len(grid[0]) - size + 1):
                    if isMagicSquare(size, i, j):
                        return size

        return 1


sol = Solution()
print(sol.largestMagicSquare(grid=[[7, 1, 4, 5, 6], [
      2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))
