from typing import List
from math import dist
from heapq import heappush, nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for each in points:
            distance = dist(each, (0, 0))
            heappush(heap, (distance, each))

        return [each for _, each in nsmallest(k, heap)]


sol = Solution()
print(sol.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(sol.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
