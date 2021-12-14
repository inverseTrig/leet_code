from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        l, r = 1, max(quantities)
        while l <= r:
            mid = (l + r) // 2
            print(f'mid: {mid}')
            # count the number of stores needed if the max distribution is mid
            # one store can has max one product only and we need to distribute all the quantities
            cnt = 0
            for x in quantities:
                # if 0<=x<=mid, cnt = 1, if mid<x<=2mid, cnt = 2
                cnt += (x + mid - 1) // mid
                print(f'cnt: {cnt}')

            # if with max distribution is mid, but number of stores needed is larger than actual stores n, then will need to increase the distribution, else we can further lower down the distribution.
            if cnt > n:
                l = mid + 1
            else:
                r = mid - 1

        return l


sol = Solution()
print(sol.minimizedMaximum(n=7, quantities=[15, 10, 10]))
