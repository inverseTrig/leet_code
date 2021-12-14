from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                ans[index] = i - index
            stack.append([i, v])

            print(f"stack: {stack}")

        return ans


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
