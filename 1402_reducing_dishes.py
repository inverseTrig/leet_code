from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        cumulative = max_satisfaction = 0
        for dish in satisfaction:
            cumulative += dish

            # if serving the dish is no longer beneficial
            if cumulative < 0:
                break

            max_satisfaction += cumulative

        return max_satisfaction


sol = Solution()
print(sol.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))
