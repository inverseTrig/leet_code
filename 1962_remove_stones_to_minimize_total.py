from heapq import heapify, heappush, heappop


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapify(heap)

        for _ in range(k):
            val = -heappop(heap)
            heappush(heap, - (val - val // 2))

        return -sum(heap)
