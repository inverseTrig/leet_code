from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        for i, val in enumerate(nums):
            while dq and nums[dq[-1]] < val:
                dq.pop()

            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


sol = Solution()
print(sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(sol.maxSlidingWindow(nums=[1], k=1))
print(sol.maxSlidingWindow(nums=[1, -1], k=1))
print(sol.maxSlidingWindow(nums=[9, 11], k=2))
print(sol.maxSlidingWindow(nums=[4, -2], k=2))
