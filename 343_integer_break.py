class Solution:
    def integerBreak(self, n: int) -> int:
        answer = 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n % 3 == 1:
            answer = (3 ** ((n // 3) - 1)) * 4
        elif n % 3 == 2:
            answer = (3 ** (n // 3)) * 2
        else:
            answer = 3 ** (n // 3)
        return answer


sol = Solution()
print(sol.integerBreak(n=10))
print(sol.integerBreak(n=11))
print(sol.integerBreak(n=12))
print(sol.integerBreak(n=2))
