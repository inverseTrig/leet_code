class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('01', '0 1').replace('10', '1 0').split()
        dp = [len(part) for part in s]

        count = 0
        for i in range(1, len(dp)):
            count += min(dp[i], dp[i - 1])
        return count


sol = Solution()
print(sol.countBinarySubstrings(s="00110011"))
print(sol.countBinarySubstrings(s="10101"))
