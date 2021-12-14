class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        ways = [0 for _ in range(len(s) + 1)]
        ways[0], ways[1] = 1, 1

        for i in range(2, len(s) + 1):
            if int(s[i - 1:i]) > 0:
                ways[i] = ways[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                ways[i] += ways[i - 2]

        return ways[-1]


sol = Solution()
print(sol.numDecodings(s="12"))
print(sol.numDecodings(s="226"))
print(sol.numDecodings(s="0"))
print(sol.numDecodings(s="06"))
