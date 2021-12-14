from typing import List
from collections import Counter


class Solution:
    def will_add(self, age1: int, age2: int) -> bool:
        if age2 <= age1 / 2 + 7 \
                or age2 > age1:
            return False
        return True

    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        result = 0
        for x in counter:
            for y in counter:
                if self.will_add(x, y):
                    if x == y:
                        result += counter[x] * (counter[y] - 1)
                    else:
                        result += counter[x] * counter[y]
        return result


sol = Solution()
print(sol.numFriendRequests(ages=[16, 16]))
print(sol.numFriendRequests(ages=[16, 17, 18]))
print(sol.numFriendRequests(ages=[20, 30, 100, 110, 120]))
