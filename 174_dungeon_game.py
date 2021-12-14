from typing import List
from functools import lru_cache


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon[0]) - 1
        n = len(dungeon) - 1

        dp = [[0] * (m + 1) for _ in range(n+1)]

        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for i in range(n - 1, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])

        for j in range(m - 1, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1] - dungeon[-1][j])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i][j+1] - dungeon[i][j], dp[i+1][j] - dungeon[i][j]))

        return dp[0][0]

# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

#         rows, columns = len(dungeon), len(dungeon[0])
#         hp = [[0]*columns for i in range(rows)]

#         # We will start at endpoint:
#         # in example we will need 6 HP to cover -5 loss
#         hp[-1][-1] = max(1, 1-dungeon[-1][-1])

#         print(hp)

#         # Completing the border lines. Excluding endpoint everywhere
#         for i in range(rows-2, -1, -1):
#             hp[i][-1] = max(1,
#                             hp[i+1][-1] - dungeon[i][-1])
#         for j in range(columns-2, -1, -1):
#             hp[-1][j] = max(1,
#                             hp[-1][j+1] - dungeon[-1][j])

#         # print(hp) to see our HealthPoint table
#         print(hp)

#         # Next we complete the remaining table
#         for i in range(rows-2, -1, -1):
#             for j in range(columns-2, -1, -1):
#                 hp[i][j] = max(1, min(hp[i+1][j] - dungeon[i][j],
#                                       hp[i][j+1] - dungeon[i][j]))

#         return hp[0][0]

sol = Solution()
print(sol.calculateMinimumHP(
    dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
