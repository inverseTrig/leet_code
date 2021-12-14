from typing import List
from sortedcontainers import SortedList


class Solution:
    def carFleet(self,
                 target: int,
                 position: List[int],
                 speed: List[int]) -> int:
        sorted_list = SortedList([(p, (target - p) / s)
                                  for p, s in zip(position, speed)])

        fleet = 0
        comp = float('-inf')
        for pos, time in sorted_list[::-1]:
            # print(f'car pos {pos} arrives in {time} s')
            if time > comp:
                # print(f'this is the start of a fleet')
                fleet += 1
                comp = time
        return fleet


sol = Solution()
print(sol.carFleet(target=12, position=[
      10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print(sol.carFleet(target=10, position=[3], speed=[3]))
print(sol.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
print(sol.carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]))
