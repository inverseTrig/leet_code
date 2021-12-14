from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int((num + 2) ** 0.5), 0, -1):
            if (num + 1) % i == 0:
                return [(num + 1) // i, i]
            if (num + 2) % i == 0:
                return [(num + 2) // i, i]


sol = Solution()
print(sol.closestDivisors(num=8))
print(sol.closestDivisors(num=123))
print(sol.closestDivisors(num=999))
