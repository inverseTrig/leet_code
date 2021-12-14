from typing import List
import heapq


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        dp = []
        for actual, minimum in tasks:
            diff, req = minimum - actual, -minimum
            heapq.heappush(dp, (diff, req, actual))

        minimum_effort = 0
        while dp:
            _, minimum, actual = heapq.heappop(dp)
            # print(f'minimum: {minimum}\tactual: {actual}')
            if minimum_effort + actual < -minimum:
                minimum_effort += -minimum - (minimum_effort + actual)
            minimum_effort += actual
            # print(f'minimum_effort: {minimum_effort}')
        return minimum_effort


sol = Solution()
print(sol.minimumEffort(
    tasks=[[1, 2], [2, 4], [4, 8]]
))

print(sol.minimumEffort(
    tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]
))

print(sol.minimumEffort(
    tasks=[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
))
print(sol.minimumEffort(
    tasks=[[1, 1], [1, 3]]
))
