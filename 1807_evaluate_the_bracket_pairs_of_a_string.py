from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        words = dict(knowledge)
        splitted = s.split('(')
        final = splitted[0]
        for i in range(1, len(splitted)):
            pre, suf = splitted[i].split(')')
            final += words.get(pre, "?") + suf
        return final


sol = Solution()
print(sol.evaluate(s="(name)is(age)yearsold",
                   knowledge=[["name", "bob"], ["age", "two"]]))
print(sol.evaluate(s="hi(name)", knowledge=[["a", "b"]]))
print(sol.evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]))
print(sol.evaluate(s="(a)(b)", knowledge=[["a", "b"], ["b", "a"]]))
