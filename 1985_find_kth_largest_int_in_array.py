from typing import List
import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = [int(i) for i in nums]
        heapq.heapify(heap)
        heap.sort()
        return str(heap[len(nums) - k])


sol = Solution()
print(sol.kthLargestNumber(nums=["3", "6", "7", "10"], k=4))
print(sol.kthLargestNumber(nums=["2", "21", "12", "1"], k=3))
print(sol.kthLargestNumber(nums=["0", "0"], k=2))
print(sol.kthLargestNumber(nums=["21", "2", "12", "982"], k=2))
