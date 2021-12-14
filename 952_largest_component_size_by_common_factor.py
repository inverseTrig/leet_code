from math import gcd
from typing import List
from collections import defaultdict


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        paths = defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if gcd(nums[i], nums[j]) > 1:
                    paths[i].append(j)
                    paths[j].append(i)

        def dfs(paths, curr: int, length: int = 0, seen: set = set()):
            if curr in seen:
                return length
            if len(seen) == len(paths):  # Seen all
                return length
            for nei in paths[curr]:
                if nei in seen:
                    continue
                seen.add(nei)
                return dfs(paths, nei, length + 1, seen)

        for node in paths.keys():
            print(dfs(paths, node))


sol = Solution()
print(sol.largestComponentSize(nums=[4, 6, 15, 35]))
print(sol.largestComponentSize(nums=[20, 50, 9, 63]))
print(sol.largestComponentSize(nums=[2, 3, 6, 7, 4, 12, 21, 39]))
