from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def minimumTime(self,
                    n: int,
                    relations: List[List[int]],
                    time: List[int],
                    ) -> int:
        pathing = defaultdict(list)
        for src, dst in relations:
            pathing[src].append(dst)

        @lru_cache(None)
        def dp(idx):
            return time[idx - 1] + max([dp(dst) for dst in pathing[idx]] + [0])

        return max(dp(i) for i in range(1, n + 1))


sol = Solution()
print(sol.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
print(sol.minimumTime(n=5, relations=[[1, 5], [2, 5], [
      3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
