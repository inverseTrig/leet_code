from typing import List
from heapq import heappush, heappop


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap = []
        for i, (costA, costB) in enumerate(costs):
            heappush(heap, (costB - costA, i, 'B'))
            heappush(heap, (costA - costB, i, 'A'))

        limit = len(costs) // 2
        A_count, B_count = 0, 0
        used = [False] * len(costs)

        cost = 0
        while heap:
            _, idx, choice = heappop(heap)
            if used[idx]:
                continue
            used[idx] = True
            if choice == 'A' and A_count < limit \
                    or choice == 'B' and B_count >= limit:
                A_count += 1
                cost += costs[idx][0]
            elif choice == 'B' and B_count < limit \
                    or choice == 'A' and A_count >= limit:
                B_count += 1
                cost += costs[idx][1]

        return cost


sol = Solution()
print(sol.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))
print(sol.twoCitySchedCost(costs=[[259, 770], [448, 54], [
      926, 667], [184, 139], [840, 118], [577, 469]]))
print(sol.twoCitySchedCost(costs=[[515, 563], [451, 713], [537, 709], [
      343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))


# 4 B
# 0 A
# 1 B
# 2 B
# 3 A
#
