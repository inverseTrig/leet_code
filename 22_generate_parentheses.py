from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def generate(s: str, left: int, right: int):
            if left:
                generate(s + '(', left - 1, right)
            if right > left:
                generate(s + ')', left, right - 1)
            if not right:
                result.append(s)

        generate('', n, n)
        return result


sol = Solution()
print(sol.generateParenthesis(n=3))
