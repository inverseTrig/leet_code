from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1

        while colors[0] == colors[right]:
            right -= 1
        while colors[-1] == colors[left]:
            left += 1

        return max(right, len(colors) - 1 - left)


sol = Solution()
print(sol.maxDistance(colors=[1, 8, 3, 8, 3]))
print(sol.maxDistance(colors=[0, 1]))
print(sol.maxDistance(colors=[1, 1, 1, 6, 1, 1, 1]))
print(sol.maxDistance(colors=[4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]))
