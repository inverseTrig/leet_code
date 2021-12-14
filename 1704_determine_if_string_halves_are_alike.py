class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        l_score, r_score = 0, 0
        for i in range(len(s) // 2):
            l_score += 1 if s[i] in vowels else 0
            r_score += 1 if s[-1 * (i + 1)] in vowels else 0

        return l_score == r_score


sol = Solution()
print(sol.halvesAreAlike(s="book"))
print(sol.halvesAreAlike(s="textbook"))
print(sol.halvesAreAlike(s="MerryChristmas"))
print(sol.halvesAreAlike(s="AbCdEfGh"))
