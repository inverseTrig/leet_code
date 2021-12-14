from typing import List
from heapq import heappush, heappop
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = []
        for key, val in counter.items():
            heappush(heap, val)

        while heap and k > 0:
            if k - heap[0] < 0:
                break
            val = heappop(heap)
            k -= val

        return len(heap)


sol = Solution()
print(sol.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
print(sol.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
