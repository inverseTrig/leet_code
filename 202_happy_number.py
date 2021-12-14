class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            nstr = str(n)

            nxt = 0
            for each in nstr:
                nxt += int(each) ** 2
            n = nxt
            if n in seen:
                return False
            else:
                seen.add(n)

        return True


sol = Solution()
print(sol.isHappy(n=19))
print(sol.isHappy(n=2))
