class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        def process_move(dominoes: str) -> str:
            result = ''
            for c in dominoes:
                result += c

            for i, domino in enumerate(dominoes):
                if domino == '.':
                    lean_left, lean_right = False, False
                    if i > 0 and dominoes[i - 1] == 'R':
                        lean_right = True
                    if i < len(dominoes) - 1 and dominoes[i + 1] == 'L':
                        lean_left = True

                    if lean_left ^ lean_right:
                        new_char = 'l' if lean_left else 'r'
                        result = result[:i] + new_char + result[i + 1:]
            if 'l' in result or 'r' in result:
                dominoes = result.replace('l', 'L').replace('r', 'R')
                return process_move(dominoes)
            return result

        return process_move(dominoes)


sol = Solution()
# print(sol.pushDominoes(dominoes="RR.L"))
print(sol.pushDominoes(dominoes=".L.R...LR..L.."))
