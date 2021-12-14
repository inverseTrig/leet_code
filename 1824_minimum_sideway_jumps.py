from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        jumps = [1, 0, 1]

        for obs in obstacles:
            if obs:
                jumps[obs - 1] = float('inf')

            for curr_lane in range(0, 3):
                if obs != curr_lane + 1:

                    next_lane = (curr_lane + 1) % 3
                    next_next_lane = (curr_lane + 2) % 3

                    jumps[curr_lane] = min(jumps[curr_lane],
                                           jumps[next_lane] + 1,
                                           jumps[next_next_lane] + 1,
                                           )

        return min(jumps)


sol = Solution()
print(sol.minSideJumps(obstacles=[0, 1, 2, 3, 0]))
print(sol.minSideJumps(obstacles=[0, 1, 1, 3, 3, 0]))
