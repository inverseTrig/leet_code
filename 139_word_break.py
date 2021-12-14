from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        n = len(s)

        can_reach = [False for _ in range(n+1)]
        can_reach[0] = True

        for i in range(n):
            if can_reach[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        can_reach[i+len(word)] = True
        return can_reach[-1]
