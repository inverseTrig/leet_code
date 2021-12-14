class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        stack = []
        max_len = 0
        for c in word:
            if c == 'a':
                if stack and stack[-1] != 'a':
                    stack.clear()
                stack.append(c)
            elif c == 'e':
                if stack and stack[-1] not in ('a', 'e'):
                    stack.clear()
                else:
                    stack.append(c)
            elif c == 'i':
                if stack and stack[-1] not in ('e', 'i'):
                    stack.clear()
                else:
                    stack.append(c)
            elif c == 'o':
                if stack and stack[-1] not in ('i', 'o'):
                    stack.clear()
                else:
                    stack.append(c)
            else:
                if stack and stack[-1] not in ('o', 'u'):
                    stack.clear()
                else:
                    stack.append(c)

                if len(stack) >= 5 and stack[0] == 'a':
                    max_len = max(max_len, len(stack))

        return max_len


sol = Solution()
print(sol.longestBeautifulSubstring(word="aeiaaioaaaaeiiiiouuuooaauuaeiu"))
print(sol.longestBeautifulSubstring(word="aeeeiiiioooauuuaeiou"))
print(sol.longestBeautifulSubstring(word="a"))
