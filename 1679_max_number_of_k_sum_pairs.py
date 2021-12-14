from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0

        mapping = defaultdict(int)
        for each in nums:
            mapping[each] += 1

        for each in nums:
            if (each in mapping and mapping[each] > 0):
                mapping[each] -= 1

                composite = k - each
                if composite in mapping and mapping[composite] > 0:
                    mapping[composite] -= 1
                    result += 1
                else:
                    mapping[each] += 1

        return result



sol = Solution()
print(sol.maxOperations(nums=[1, 2, 3, 4], k=5))
print(sol.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
