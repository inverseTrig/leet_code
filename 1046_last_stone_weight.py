from typing import List
from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * weight for weight in stones]
        heapify(heap)

        while heap:
            stone1 = heappop(heap)
            if not heap:
                return -1 * stone1
            stone2 = heappop(heap)
            if stone1 > stone2:  # Note, negative numbers.
                stone1, stone2 = stone2, stone1
            heappush(heap, stone1 - stone2)
        return 0


sol = Solution()
print(sol.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
print(sol.lastStoneWeight(stones=[1]))
