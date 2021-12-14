from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        print(envelopes)

        dp = list()
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
            print(dp)
        return len(dp)



sol = Solution()
i = sol.maxEnvelopes([[4, 4], [6, 4], [6, 7], [2, 3], [5, 5], [6, 5]])
print(i)