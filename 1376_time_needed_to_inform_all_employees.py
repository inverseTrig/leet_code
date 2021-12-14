from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self,
                     n: int,
                     headID: int,
                     manager: List[int],
                     informTime: List[int],
                     ) -> int:
        pathing = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                pathing[m].append(i)

        # for k, v in pathing.items():
            # print(f'{k}: {v}')

        def bfs(curr: int, time: int):
            if curr not in pathing:
                return time

            return max([bfs(dest, time + informTime[curr])
                        for dest in pathing.get(curr)])

        return bfs(headID, 0)


sol = Solution()
print(sol.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))
print(sol.numOfMinutes(n=6, headID=2, manager=[
      2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
print(sol.numOfMinutes(n=7, headID=6, manager=[
    1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]))
print(sol.numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4,
4, 5, 5, 6, 6], informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))  # noqa
print(sol.numOfMinutes(n=4, headID=2, manager=[
    3, 3, -1, 2], informTime=[0, 0, 162, 914]))
