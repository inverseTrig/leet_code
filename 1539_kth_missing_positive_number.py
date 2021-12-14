from bisect import bisect
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = bisect(arr, k)
        while i:
            k += i
            arr = arr[i:]
            i = bisect(arr, k)
        return k


sol = Solution()
print(sol.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(sol.findKthPositive(arr=[1, 2, 3, 4], k=2))
