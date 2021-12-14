class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = int(len(encodedText) / rows)
        divided = [encodedText[k * N:(k + 1) * N] for k in range(rows)]

        for i, part in enumerate(divided):
            divided[i] = part[i:] + part[:i]

        decoded = ''
        for i in range(N):
            for part in divided:
                decoded += part[i]

        return decoded.rstrip()


sol = Solution()
print(sol.decodeCiphertext("ch   ie   pr", 3))
