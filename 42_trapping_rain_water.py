from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = [0] * N, [0] * N
        left[0], right[-1] = height[0], height[-1]
        for i in range(1, N):
            left[i] = max(height[i], left[i - 1])
            right[-i - 1] = max(height[-i - 1], right[-i])

        water_trapped = 0
        for i in range(1, N):
            water_trapped += min(left[i], right[i]) - height[i]
        return water_trapped


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
