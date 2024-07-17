class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                min_sum = min(triangle[i + 1][j], triangle[i + 1][j + 1])
                current_val = triangle[i][j]
                triangle[i][j] = current_val + min_sum

        return triangle[0][0]

