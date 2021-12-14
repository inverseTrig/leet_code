from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        ignore = set()
        for each in counter:
            if counter[each] > 1:
                ignore.add(each)

        idx, counted = 0, 0
        while counted < k:
            if idx >= len(arr):
                return ""
            if arr[idx] not in ignore:
                counted += 1
                if counted == k:
                    return arr[idx]
            idx += 1

        return


sol = Solution()
print(sol.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2))
print(sol.kthDistinct(arr=["aaa", "aa", "a"], k=1))
print(sol.kthDistinct(arr=["a", "b", "a"], k=3))
