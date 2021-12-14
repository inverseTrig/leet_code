from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter([each % k for each in arr])

        for i in range(k):
            composite = -i % k
            while counter[i]:
                counter[i] -= 1
                if not counter[composite]:
                    return False
                counter[composite] -= 1

        return True


sol = Solution()
print(sol.canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
print(sol.canArrange(arr=[1, 2, 3, 4, 5, 6], k=7))
print(sol.canArrange(arr=[1, 2, 3, 4, 5, 6], k=10))
print(sol.canArrange(arr=[-10, 10], k=2))
print(sol.canArrange(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3))
