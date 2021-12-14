from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)

        times = 0
        for val, count in counter.most_common():
            if n <= len(arr) // 2:
                break

            n -= count
            times += 1

        return times


sol = Solution()
print(sol.minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(sol.minSetSize(arr=[1, 9]))
print(sol.minSetSize(arr=[1000, 1000, 3, 7]))
print(sol.minSetSize(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
