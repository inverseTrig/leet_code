from bisect import bisect
from typing import List
from collections import defaultdict, deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rained = defaultdict(lambda: -1)
        dry_days, move = deque([]), [-1] * len(rains)

        for i, city in enumerate(rains):
            if not city:
                dry_days.append(i)
            else:
                if rained[city] > -1:
                    if not dry_days:
                        return []

                    day_rained = rained[city]
                    _idx = bisect(dry_days, day_rained)
                    if _idx >= len(dry_days):
                        return []

                    dry_idx = dry_days[_idx]
                    dry_days.remove(dry_idx)
                    move[dry_idx] = city

                rained[city] = i

        while dry_days:
            dry_idx = dry_days.popleft()
            move[dry_idx] = 1

        return move


sol = Solution()
print(sol.avoidFlood(rains=[1, 2, 3, 4]))
print(sol.avoidFlood(rains=[1, 2, 0, 0, 2, 1]))
print(sol.avoidFlood(rains=[69, 0, 0, 0, 69]))
print(sol.avoidFlood(rains=[0, 1, 1]))
print(sol.avoidFlood(rains=[1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3]))
