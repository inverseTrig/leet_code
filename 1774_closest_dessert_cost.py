from typing import List


class Solution:
    def closestCost(self,
                    baseCosts: List[int],
                    toppingCosts: List[int],
                    target: int,
                    ) -> int:
        cost = 0



sol = Solution()
print(sol.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10))
print(sol.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18))
print(sol.closestCost(baseCosts=[3, 10], toppingCosts=[2, 5], target=9))
print(sol.closestCost(baseCosts=[10], toppingCosts=[1], target=1))
