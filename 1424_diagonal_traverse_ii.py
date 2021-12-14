from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        digested = defaultdict(list)
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                digested[i + j].insert(0, val)

        result = []
        for _, e in digested.items():
            result.extend(e)
        return result


sol = Solution()
print(sol.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [
      6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
print(sol.findDiagonalOrder(
    nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))
print(sol.findDiagonalOrder(nums = [[1,2,3,4,5,6]]))
