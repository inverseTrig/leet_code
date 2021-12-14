from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = max(area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return area

sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))