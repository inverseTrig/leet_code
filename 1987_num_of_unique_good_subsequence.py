class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        ends_with = [0, 0]
        has_zero = 0
        mod = 10**9 + 7
        for c in binary:
            if c == "1":
                ends_with[1] = (sum(ends_with) + 1) % mod
            else:
                ends_with[0] = sum(ends_with) % mod
                has_zero = 1

        return (sum(ends_with) + has_zero) % mod
