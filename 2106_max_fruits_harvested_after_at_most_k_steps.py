from typing import List


class Solution:
    def maxTotalFruits(self,
                       fruits: List[List[int]],
                       startPos: int,
                       k: int) -> int:
        fruit_mapping = {idx: amount for idx, amount in fruits}

        fruit_count = []
        for i in range(startPos - k, startPos + k + 1):
            fruit_count.append(fruit_mapping.get(i, 0))

        left, right = sum(fruit_count[:k + 1]), sum(fruit_count[k:])
        highest_seen = max(left, right)

        distance_after_turn = 1
        for i in range(0, k - 2, 2):
            left = left \
                - fruit_count[i] \
                - fruit_count[i + 1] \
                + fruit_count[k + distance_after_turn]
            right = right \
                - fruit_count[~i] \
                - fruit_count[~(i + 1)] \
                + fruit_count[k - distance_after_turn]
            highest_seen = max(highest_seen, left, right)
            distance_after_turn += 1

        return highest_seen


sol = Solution()
print(sol.maxTotalFruits(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4))
print(sol.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [
      6, 2], [7, 4], [10, 9]], startPos=5, k=4))
print(sol.maxTotalFruits(fruits=[[0, 3], [6, 4], [8, 5]], startPos=3, k=2))
