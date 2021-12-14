from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        visited = set()

        def jumpable(position: int, jump: int) -> bool:
            if position + jump not in stones or (position, jump) in visited:
                return False
            if position + jump == stones[-1]:
                return True

            visited.add((position, jump))

            return jumpable(position + jump, jump) or \
                jumpable(position + jump, jump - 1) or \
                jumpable(position + jump, jump + 1)

        return jumpable(stones[0], 1)


sol = Solution()
print(sol.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]))
print(sol.canCross(stones=[0, 1, 2, 3, 4, 8, 9, 11]))
