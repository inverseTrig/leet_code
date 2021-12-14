from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        maxwidth = max([right for _, right, height in buildings])
        print(maxwidth)

        skyline = [0] * (maxwidth + 1)

        for left, right, height in buildings:
            skyline[left] += height
            skyline[right] -= height

        print(skyline)

        for i in range(1, len(skyline)):
            if skyline[i]:
                skyline[i] = max(skyline[i - 1], skyline[i])
            else:
                skyline[i] += skyline[i - 1]

        print(skyline)


sol = Solution()
print(sol.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [
      5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(sol.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
