from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if min(len(nums1), len(nums2)) * 6 < max(len(nums1), len(nums2)):
            return -1

        n_total, m_total = sum(nums1), sum(nums2)
        if n_total > m_total:
            return self.minOperations(nums2, nums1)

        available_moves = Counter([num - 1 for num in nums2]
                                  + [6 - num for num in nums1])

        moves_made = 0
        current_move = 5
        while n_total < m_total:
            if available_moves[current_move] == 0:
                current_move -= 1
            n_total += current_move
            available_moves[current_move] -= 1
            moves_made += 1

        return moves_made


sol = Solution()
print(sol.minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]))
print(sol.minOperations(nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6]))
print(sol.minOperations(nums1=[6, 6], nums2=[1]))
