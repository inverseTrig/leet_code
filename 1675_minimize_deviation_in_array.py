from typing import List
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heap = [-i if i % 2 == 0 else -i * 2 for i in nums]
        heapq.heapify(heap)

        result = float('inf')
        minimum = -max(heap)

        while len(heap) == len(nums):
            popped = -heapq.heappop(heap)
            result = min(result, popped - minimum)
            if popped % 2 == 0:
                minimum = min(minimum, int(popped / 2))
                heapq.heappush(heap, int(-popped / 2))

        return result



sol = Solution()
print(sol.minimumDeviation(nums=[1, 2, 3, 4]))
print(sol.minimumDeviation(nums=[4, 1, 5, 20, 3]))
print(sol.minimumDeviation(nums=[2, 10, 8]))
print(sol.minimumDeviation(nums=[9, 4, 3, 6, 2]))
print(sol.minimumDeviation(nums=[3, 5]))
