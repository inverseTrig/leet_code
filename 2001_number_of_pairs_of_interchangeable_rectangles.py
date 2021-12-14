from typing import List
from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        result = 0
        counter = defaultdict(int)
        for i in range(len(rectangles) - 1, -1, -1):
            numer, denom = rectangles[i]
            div = numer / denom
            result += counter[div]
            counter[div] += 1

        return result


sol = Solution()
print(sol.interchangeableRectangles(
    rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]]))
print(sol.interchangeableRectangles(rectangles=[[4, 5], [7, 8]]))
