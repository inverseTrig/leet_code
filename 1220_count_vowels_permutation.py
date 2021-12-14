class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = [1, 1, 1, 1, 1]
        mod = 10 ** 9 + 7
        for _ in range(1, n):
            next_count = [count[1] + count[2] + count[4] % mod,
                          count[0] + count[2] % mod,
                          count[1] + count[3] % mod,
                          count[2] % mod,
                          count[2] + count[3] % mod,
                          ]
            count = next_count
        return sum(count) % mod


sol = Solution()
print(sol.countVowelPermutation(n=2))
print(sol.countVowelPermutation(n=5))
