from typing import List
from heapq import heappush, nsmallest


class Solution:
    def kSmallestPairs(self,
                       nums1: List[int],
                       nums2: List[int],
                       k: int) -> List[List[int]]:
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                heappush(heap, (n1 + n2, n1, n2))

        pairs = [(n1, n2) for _, n1, n2 in nsmallest(k, heap)]
        return pairs


sol = Solution()
print(sol.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(sol.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
