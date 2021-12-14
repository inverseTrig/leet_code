from math import ceil


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        final_score = 0
        for i, c in enumerate(word):
            if c in ['a', 'e', 'i', 'o', 'u']:
                index = i if i < ceil(n / 2) else abs(n - i) - 1
                final_score += (index + 1) * n - (index ** 2 + index)
        return final_score


sol = Solution()
print(sol.countVowels(word="noosabasboosa"))
