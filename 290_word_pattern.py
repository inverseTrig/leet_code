class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = dict()

        P, S = list(pattern), s.split(' ')

        if len(P) != len(S):
            return False

        for i in range(len(P)):
            if (P[i] in word_dict and word_dict[P[i]] != S[i]) \
                    or (S[i] in word_dict.values() and P[i] not in word_dict):
                return False
            else:
                word_dict[P[i]] = S[i]
        return True


sol = Solution()
print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))
print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))
print(sol.wordPattern(pattern="abba", s="dog dog dog dog"))
