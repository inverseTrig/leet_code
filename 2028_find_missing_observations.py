from typing import List
from math import ceil


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing = (mean * (len(rolls) + n)) - sum(rolls)
        if missing < n or missing > n * 6:
            return []

        dice = []
        while missing:
            candidate = ceil(missing / n)
            missing -= candidate
            n -= 1
            dice.append(candidate)

        return dice


sol = Solution()
print(sol.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
print(sol.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
print(sol.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
print(sol.missingRolls(rolls=[1], mean=3, n=1))
