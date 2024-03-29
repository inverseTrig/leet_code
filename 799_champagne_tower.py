
class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        res = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + \
                    max(res[i - 1] - 1, 0) / 2.0
                print(res)
        return min(res[query_glass], 1)


sol = Solution()
print(sol.champagneTower(poured=1000, query_row=33, query_glass=17))
