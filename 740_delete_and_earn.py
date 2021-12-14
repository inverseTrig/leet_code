from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = [0] * 10001
        for n in nums:
            counter[n] += n
        return self.rob(counter)

    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
