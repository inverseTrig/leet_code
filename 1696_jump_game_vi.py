from typing import List
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n-1])
        for i in range(n-2, -1, -1):
            print("-- START OF LOOP i = {} --".format(i))
            print("Deque: {}".format(deq))
            if deq[0] - i > k:
                deq.popleft()
                print("-- Popping left: {}".format(deq))
            nums[i] += nums[deq[0]]
            print("Nums[{}]: {}".format(i, nums[i]))
            print("Nums[]: {}".format(nums))
            while len(deq) and nums[deq[-1]] <= nums[i]:
                deq.pop()
                print("-- Popping: {}".format(deq))
            deq.append(i)
            print("End DEQ: {}".format(deq))
            print("-- END OF LOOP --\n")
        return nums[0]


sol = Solution()
# print(sol.maxResult(nums=[10, -5, -2, 4, -1, 3], k=3))
print(sol.maxResult(nums=[1, -5, -20, 4, -1, -3, -6, -3], k=3))
