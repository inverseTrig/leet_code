from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        height, N, existing = max(nums), len(nums), sum(nums)
        can_add = N - 1

        remainder = (height * N - existing) % can_add
        turns = (height * N - existing) // can_add
        while can_add and (remainder != 0
                           or (height - min(nums) >= turns)):
            height += 1
            remainder = (height * N - existing) % can_add
            turns = (height * N - existing) // can_add

        return turns if can_add else 0


sol = Solution()
print(sol.minMoves(nums=[1, 2, 3]))
print(sol.minMoves(nums=[1, 1, 1]))
print(sol.minMoves(nums=[-100, 0, 100]))
