import heapq

from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_round = [dist[i] / speed[i] for i in range(len(dist))]
        heapq.heapify(arrival_round)

        print(arrival_round)

        count, round_count = 0, 0
        while arrival_round:
            monster_arrival = heapq.heappop(arrival_round)
            if round_count >= monster_arrival:
                break

            count += 1
            round_count += 1

        return count if count else 1


sol = Solution()
print(sol.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
print(sol.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
print(sol.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))
print(sol.eliminateMaximum(dist=[4, 2, 3], speed=[2, 1, 1]))
print(sol.eliminateMaximum(dist=[3, 5, 7, 4, 5], speed=[2, 3, 6, 3, 2]))
