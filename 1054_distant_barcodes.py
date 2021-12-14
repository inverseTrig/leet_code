from typing import List
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        res = [0] * len(barcodes)
        i = 0
        for val, count in counter.most_common():
            for _ in range(count):
                if i >= len(barcodes):
                    i = 1
                res[i] = val
                i += 2
        return res


sol = Solution()
print(sol.rearrangeBarcodes(barcodes=[1, 1, 1, 2, 2, 2]))
print(sol.rearrangeBarcodes(barcodes=[1, 1, 1, 1, 2, 2, 3, 3]))
