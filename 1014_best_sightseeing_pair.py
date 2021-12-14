from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = values[0]
        index = 0

        for i in range(1, len(values)):
            result = max(result, values[index] + index + values[i] - i)
            if (values[index] + index < values[i] + i):
                index = i
        return result


sol = Solution()
print(sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
