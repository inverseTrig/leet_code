from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        cumulative = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cumulative[i + 1][j + 1] = mat[i][j] \
                    + cumulative[i][j + 1] \
                    + cumulative[i + 1][j] \
                    - cumulative[i][j]

        result = [[0] * (len(mat[0])) for _ in range(len(mat))]
        for i in range(len(mat)):
            i1, i2 = max(0, i - k), min(len(mat), i + k + 1)
            for j in range(len(mat[0])):
                j1, j2 = max(0, j - k), min(len(mat[0]), j + k + 1)
                result[i][j] = cumulative[i2][j2] \
                    - cumulative[i1][j2] \
                    - cumulative[i2][j1] \
                    + cumulative[i1][j1]

        return result


sol = Solution()
print(sol.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=2))
