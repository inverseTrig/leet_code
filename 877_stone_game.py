from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def recursiveChoice(
                left: int = 0,
                right: int = len(piles)-1
                ) -> int:
            if right - left <= 0:
                return 0

            front = piles[left] - recursiveChoice(left + 1, right)
            end = piles[right] - recursiveChoice(left, right - 1)

            return max(front, end)

        return recursiveChoice() > 0

sol = Solution()
print(sol.stoneGame(piles=[3, 7, 2, 3]))
