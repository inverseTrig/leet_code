# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self,
                            target: int,
                            mountain_arr: 'MountainArray',
                            ) -> int:
        n = mountain_arr.length()
        # Find the peak of the mountain
        l, r = 0, n
        while (l < r):
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                peak = l = m
            else:
                r = m

        # Find left side
        l, r = 0, peak
        while (l <= r):
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val > target:
                r = m
            elif val < target:
                l = m
            else:
                return m

        # Find right side
        l, r = peak, n
        while (l <= r):
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                l = m
            elif val > target:
                r = m
            else:
                return m

        # Didn't find it
        return -1


sol = Solution()
print(sol.findInMountainArray(array=[1, 2, 3, 4, 5, 3, 1], target=3))
print(sol.findInMountainArray(array=[0, 1, 2, 4, 2, 1], target=3))
