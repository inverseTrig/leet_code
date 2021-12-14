class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        steps = 0
        for each in word:
            if each == prev:
                steps += 1
            else:
                steps += self.get_dist(prev, each) + 1
            prev = each
        return steps

    def get_dist(self, a: str, b: str) -> int:
        if (ord(a) >= ord(b)):
            b, a = a, b
        return min(abs(ord(b) - ord(a)), abs(26 - ord(b) + ord(a)))


sol = Solution()
print(sol.minTimeToType(word="abc"))
print(sol.minTimeToType(word="bza"))
print(sol.minTimeToType(word="zjpc"))
