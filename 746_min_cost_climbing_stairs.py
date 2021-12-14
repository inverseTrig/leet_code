from typing import List
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache(maxsize=None)
        def recursive(n: int) -> int:
            if n < 0: return 0
            if n == 0 or n == 1: return cost[n]
            return min(cost[n] + recursive(n-1), cost[n] + recursive(n-2))

        return min(recursive(len(cost) - 1), recursive(len(cost) - 2))


sol = Solution()
print(sol.minCostClimbingStairs(cost=[10, 15, 20]))
