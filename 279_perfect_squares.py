from math import sqrt, floor


class Solution:
    def numSquares(self, n: int) -> int:
        count = 0
        while n > 0:
            root = floor(sqrt(n))
            n -= root ** 2
            count += 1
        return count
