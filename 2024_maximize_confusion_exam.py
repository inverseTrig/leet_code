import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = collections.Counter()
        max_window = 0
        i = 0
        for j in range(len(answerKey)):
            d[answerKey[j]] += 1

            while d['T'] > k and d['F'] > k:
                d[answerKey[i]] -= 1
                i += 1

            max_window = max(max_window, j - i + 1)

        return max_window


sol = Solution()
print(sol.maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(sol.maxConsecutiveAnswers(answerKey="TFFT", k=1))
print(sol.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))

"TFFFFTTFTFFTFFTTFTFTTTFTFTTTFTFFTFTFTTFTTFFTFFFFTFFFTFFFFFTTTFTTFTFTTFTFTTFTFFFTTTFTTTTTTFTTTTTFTFTTFFFFTTFTFTFFFFTFTTFTTTTTFTFTTTFFTFFTFFFFTTFTFTTFTFFFTFTTFFFFFTTTTTFFFFTFFFFTTTTTTFTTTFFFFTFFTFTFFFFFTTFFTFFFTTFTFFTFFTTFTFFTFFFTTFTTFTFFTTFFFFTTFFTTFTTTFFFFFFTTFTTFTTTTFFTFTFTFTFTTFTTFTFTFFTFTFTTTFTTTFFFTFTFTTFFTFTTFFTTTTFFTFFTFFTFFFTTFTTTTTFTFTFFFTTTTTFFFFTTFTFFFTFTFTFTTFFTTFTFFFTTFFFFFTTTFFTFTFTTTTTFTTTTFFFFFFTFFFTTFTTFTTFTFFFFTFTFFFFTTFFFTTFTTFTFFFFTFFTTFFFFFTTTFFFFTTFTFFFFTTFTFTFFTFFTFTTTFTFFTTTTTFTFFFTTTTTFFFFTFTFFTTTFFTFTTTTTFFFFTFTFFTTTTTFFFTTFTTFTFTFFFFTFFFTTFTTFFTFFFTTFTTTFFTTTFFFFTTFTFTTTTTFTFTTTFTTFTFTFTTTTTFTFTTTTFTFFTTFTFFFFTFFTTFTFTTTFTTFFTFFFTTTTTTFFTFFTFFFFFTTTTTTFTFFTFFFFTFTTTFFFFFTFFFFFFTFTTFFFTTTFFTTTFTFTFTTFFFTFTFFTTTFTTTTTFTFFFFTTFFFTTFTFTFFFFFTTFTTTFFFFFFTTTTTTTFFTTFTTTFFTFFFTFTFTFTTFFTFTFTTTTFFTTFTFTFFTFTTTFTTTFFTTTFFTTFFFTFTFTTTFTTFFFFTFFFFFTTTFFTTFFTTTTFFFTTTFFFTTTFFFFTFTTFFTTTTTTTFTTFFFTTFTTFFFTTTTFTFTFTFTFFTTFTFTFFFTFTTFTFTFTTTTTTFTTFFFFFTFTFFTFFTFFFTFFFFFFTFTTFFTTFTTFTTFFTTTFTTTFTTTTFFTTTFTTTTTFTFFTTTFFTFFTTTTFFFFFTTTFFTTFTTTFFTFFTFFFTFFTFTTTTFTFTTFFTFTFFTTFFTTFFFTFFTFFFFFFFTFFFFTFTTTTTFTTFTFTTTFTTTFTFTFTTTTFTFTFTFFFFFFFFFTTTTTTFTTTFTFTTTFTTTTTFFFTFFTTFFFFTTFTFFFFFFFFTFTTFFTFTTFTTTTTFTTTFFTTFFFTFTFTFTTTFTTTTTFTFTFTFFTFFTTTFFTFTFFFFTFTTTTFFFFFFFTFFTFFTTFFTTTTFFFTTFFFTTTFTFFTFFTFFFFFTFFFTTTTTFFTFFTTTTTTTTFTFTFFFTTTFTFTFFTTFFFFTTTFTFFFTFTFTTFTTTTTTFTTFTFTTTTTTTFTFFFFFTTFTTTTTTFFFFTTFTTTTTTFTTFFTFTFTFFTFTFFFTTTTTFFFTTFTTFTTFTFFFFTFFTTTFTFFFTTTFFFTFFFTFTFTTTTFFTTTFTFTFFFFTFFFFFFFFTTFFTFFFTTTTFTTFFFTTFTFTFFTTFFFTFTFFTFFFTTTFTTFFTFFFTTFFTTFTFFTTFFFFFFFFTFFTTTTTTTTTFTFFFTFFTFTFTFTTFFTTTTTTTTTTFTFFTTTFTTFTTFFFFFTFTTFFFFFTTFFTFFFTFFTFFFTFFTFFFTTTFFFTTFTFFFFTTTTTTFFFTTFFTFTFFFFFTTFFTTTFTFFTFTTFTFTTFFTFFTTFTFTFTFTTFTTFFTTTFTTTFTTFFTTTTTFFTFTFTTTFFFFTFFFTTTTTTTFTTTFTTFFTFFFTTTFTFFFFTTFFFTTTTTTTTFTFFFFFTFTFTFFFFTTTTTFTFFTFFTFFFFTTTFFFFFFFTFFTFTFFTFTTTFFFFTFFTTFTFTFFFTFFTTTFTFTTFTTFFFTTFFFFTTFFFTFFFTTTTTFFTFFTFTTTFTFTFFFTFFFFTFTTFFFTFFFFFTTFTTFFFTTFTFTFFTFFTTFFTTFFTFFFTTTTFTTTFFFFFFTFFFFFFFTTTFFTFFFTTFTFFFFFTFTTTFTFFTTTTTFTFFTFFTFFTTFTTFTTTTTTFFTTTTTTTFTFFFTTTTFFTTTFFTTFFFFTFFFTTFFTTFTTFFFTTTFFTTTFTFTFFFTFFFTTTFTFFFFFFTFFFTTTFFTFTTTFFFFTFTTTFFTFTTTTTTFFTFTFTFFFFFTTFFFTTFTFFTFFTTTTFTTTFFFTFTTFTFTFFFTFTTFFTFFFTTFFTFTFTFFTTTTTFFTFTFTTFFTFFTFTFTFTFFFTFTFTFTTFFFTTFFFTFTFFFTTTFFFFTTFFFTFFTFFTTTFTFTFTFTFTTFFFFFTTFFFFFTTFTTFTTFTTFFFFTFFTTFTFFFFFFTFTTFTFTTTTFTTFTTTFFFTFFFTTTTTTTFFFFFFFFFTTTFTTFFTTFFTTTFFFFTTTTFFFTTFTFTTFFTTTTTFFFTTTTFFTFFFFFFTFTTTFTTTFFFFFFFTTTFFTFTTTFFFTFFFTFFFFFFFFFFFFFFFFTFTFTTTFTFTFTTFFFFTFTFFFTFFFTTTFTTFFFTFTTTFFTTTTTTFTFTFTTFFTFTFTFFTTTTTTFFFFFFTFTFFFFTTFFFTTTTFFFFTFTFFFFFFTTTFTFTTTTFTFFFTFTTTFTTFTFTTTTFFTFTFTFTFTFTTTTFTFFTTTFFTTFTTFTFTFFFFFTTFFFFTFFTTFTTFTTFFFFFFFTTTFFFTFTTFFFFFTTTTTTTFFFFFTTTTTTFFFTFFTFFFTFTTTFTFTTFTFTFTTTFTTFTFFTTTTFTTTFTFTTTFFFTTTFTTFFFTFTFFTFFTFTTFFTTFFTTTTTTFTTTTTFFTTFFTFFTFTTTTFFTFFTFFTTFTTTTTFTFFFTTTTFTTTFTFTFTFFFFTFTTTTFTTTTTTTFFTFFTFFTTTTFTFFTTTFTFFTFFFFTFTFTFFTFTTTTTTTFFTTTTFTTTFTTTFTTTTFFTFFTTTFTFTFTTTTTTTFTFTFFTTTTTTFTFTFFTFTTTFFFTTFTFFFTTFFTTTFTTFTTFFFFTFTTFFTFFTFTTFTFTFFTFFTTTFTTTFTFTTFTTFTFTFTFTFTFFTFTFTTTTFTTFTTFFFTFTFFTFTFTTTFFFTFFFTFTTFTTFFTTTTFFFTTTFFFFFTTTFTFTTTTTFTFTTFFTTFFTTFFTFFFTFFTFTTFTTTTFFFFTFFFTFTFFTFTTFFTTTTFFTFTFFTFTTFTFFFFTFTTFTFFFFTTTTTTTFTFFFFTFFFFTTTFFFFTTFTFTTFTTFTTFFFFFFTTTFFFTFFFTTTTTFFTTTFTTTFTTFFTFTFFFTTTTFTTFTFFTTTFTTFFFTFTFFFFFFFTTFTFFFTFFFFFFTTTTFTTTTFFFFTFFFFTTFTFFFTTTTTFFFFFFFFFFFTTFFFTFFTTFFTTTFFFFFFTTFFTTTTFFTTFTTFFTTTTFTFFTTFFTTTFFFFTFTFTTFFFFTTFTFFFFTFFTFTFFTFFTTFTFTFFFTTTTFTFFFTFFTFFFTFTTTFFFFTFFTFFTFTTTFTFFFFTTFTTFFTTFTFFFTTTTFTFTFTFTTFFFTTTTTTTFTFTFTFTFFTFTFFTFTFTFFTFFFFTTFTTTTTFFFTTTTFTTFTTTFTTTFTTTFFFFFFFTTFTFTFFTFTFFFTFTTFTTTTFTFFFFFTTFTTTFTTFFFFFTTFFTFTFTTTFFTFFTTTTTTTTTTTTTFFFFTFTTTFTFFFFFTTFTFFTTFTFFTFFTTTFTFFFTFTTFTTTFTTTFTFFTFTFFFFTFTFTTTFTTTFFTTFFFTFFTFTTTTTTTTTTTTTTFTFFTTFFFTFTTTTFTFFTFTTFTTTTTFFTFFFTTFFTFFFFFTTFFTFTTTTFTTTTFTTFFFFTTTFTTTFTTTFFTTTTTTFFFTTTFFFFTTTTFFTFFFTTFTFFFFTTTTFTTTTTFTTTFFFFFTFTFTTFTTTTFFFFFFTTTFFTTTTFFTTFTFFFTFFFFFFTFTTFTTTTTFTFFFFFTFFTFFFTTFTFFFFTFFTTFTFFTTTFTFFTFFFFFTTFFFFFTTTTFTTTTFFTFTFTFFFFTTTTFTTFFFTFFTFTTFFTFFTFFTFTTTFFFFFTTTTTTFTTTTTFFTFTTTTFTTTTTTFTFTFFTTTTTTFTFTFTTFTFFTTFFFTTFTTTFTFTFTTFFFFFTTFTFTTTFTFFFTFFTTFTFFTTTFFTTTTFTFTFFFTTTTFFTTTFFTFTFFTTFFFTFTFTTTFFTFTTTTFTFFFTTFFTFFFTTTTTFFTTFTFTFFTTFTFFFFTFTTTFTTTFTFTTTFTTFTFFFFFFFFFFFFTTTFTTFFFTFFFFTFFTFTFTFTFFTTTFFTTFFTTFTFTTFFTFTTTTFFTFTFTFTFFTFFTTTTFTTFFTTFFFTFTFFTTTTTTTTTTFTFFTFFTTFTFFFFFTTTTFFFTTFTFTTTFFTFFTTFFFTFFTFFFTTFTFFTTTTFTFTTFTFFTTTTTFTFTFFTFFTTTFTFTFTFFTTTFFFFFFTFFTTTTFTFTTTFFFFTTFTTTFFTFTTTTFFTFFFTTFFFFFTTFTFFTFFFTFTTFTFFTFTFFFFTFFFFFFTFFFTTFFTTTTTFTTTFTFFFTTTTFFTTTTFTFTFFTFTTTFFTTFFFTFTTFTTFTFFTFFFFTFFFTTFTTTTFTTTTFFFFTTTFFFTTTFFTFFFTFTFFTTFFTFFFTTFFFTTTTTTTTTFFTFTTTTTTFFTFTFFTTTFFFFTFTTTTFTTTFFFTTTFFTFFTFTTFTFFTTTFTTTTTTTFTTFTTTFTTTFTFTFTTTTTTTFTTFTTTTFFTTTTTFTFTFTTTTFFFTFTFFFFFFTTFFTFTTTTTFTTFTFTTTTTTFTFTTTFFTTFFTTTTTTFTFTFFTTTTFFFFTFFFFFFFFTFFFFFFFFTTTFFFTTFTFTTTTTFTTTFTTTTFFFTFTFFFTTFTTTTFTFFFFFFFFFTTFTTTTTTFFTTFTFFTTTFFFFFFFTFFFTFFTTFFFFTFFFFFFFTTFFTTTFTFFFFFFTTFTTFFFFFFTTFTTFFFTTFTTTFFFTFTTFTTTTFFFFTFFTTFTFTFTFTTTTFTTFTTTTFFFTFFFFFFTFTFFFFTTFFFFFFFFTTFFFTFFFFTTFTFTFFFFFTFTFTFFFTTFFFTFTFFFTTTTTFFFFFFTFFTFTTFTTFTFTTFTFFTFTFFTTTFTFTTTFTTTFFFTTFTTTTFTFTTFTFTFFFTTTFTFTTFFFTTTTFFTFFFTTFTTTTFFTTTTTFTTFFTFFTTTFTFTTFFTTFTTTFFTTTFFFTFTFFFFTTTTFTTFFTTTTTFTFTFFTTFFTTFTTFTFFFTTFTTFTFFTFTTFTTTTFFFTTTFTTFTFTFTTFFTFFFTTTFFFTFTFTTTTFTFFFFFFTTFFFFFFTFFFTTTFTFTFTFFTTTTFFTTTFFFFTTFFTTFFFTTTTTTFTTTTFFFTFFTFTFTTFFTFFTTTTFTFTTTFFTFTTTTTTTTTFFFTTTTTFTFFFFFTFTTTFTFTFTTFTFFFTTFTTFTTTTTFTFFTFTFTFFFFFTFFFFTTFTTFFFFTFTTTTTFTTTFFFTTFTTTFFFTTFFTFTFFFTFTFTTFFFTTTTTFFTTTTFFFTTFTFFTTTTFFTTTTTFFFTFTTTFFTTTTTFTFTFTTTTTTTFFTFFFTTFFFTFTTFFTFTTTFFTFTFTTTTTTFFFTTTFTTFFTTTFFTFFFTFFFTFTFTTFTTTTTTTFFFTFTTTFTFFFTTFTTFTFFTTTFFFTFTFFTTTTTTTTTFFTTTTFTFTTTFTFTFFTTFTTFTTFTTTFFFTFTTFFFTTTTTTFFFFTTFTFTFTTFTTFFFFTFFTTFTTTFFTFTTFFFFFFTTFFTFTTFTTTFFTTFTTTTTFFTFFFFTFFTFFTFTFTTFTTTFFFTFTFFFFTTTTTFTFFTFFFTTTTFFFFTFFFTFFTTTTTFFTTFFFFTFTTTFFFFTTFFFTFFTTFTFTFTTFFFTTFTTFTTTTFTTFTFTTFTTTTFFTTFTTFTTFFFTTTTTFFTTTFTFTFFFFTFTTTTTFFFTFFFFTFFFTFTTTFTFTTTFFTTTFTFTTTTFFFFTFFFTFTTFFFFFFTTFTFTFFFFFFTFTFTTTTTTFTTFTFTFFFFFFTFFTTFFFFFTTTFTFFTTFFFTFTTTTTFFFTTFFFTTFFTFFFFTFFTFFFFTFTTTTFFTTTFFTFFTFTTFFTTTFTTTFFFTTTTTTFFFFFFFFFTTTTTFFFFFTTTTFTTFTFTTFTTTFFTTFFTFTTFFFTTFTFTFFFTFTTTFTFFTTTFTTFTTFTFTTFFFFFTFTFTFFTTTTTTTFTTTTTFFTFFFTFFFTTFFFTFTFTTTTFFTTFFTFTTFFFTFFFTFFFFTTTFFFTFFFFFFFFFFTFFTTFTTFFFFFTFTFTTTTFFFTFTFTTFTFFTTTFFFTTFFFFTFFTTFTTFTFFTFFTTFTTTFFTFFTTFFFFFFTTFTFTTTTFTTTTFTTFTFTTTFFFFTFFFFFTFFTTFFFTFTTTTFTFFTFFFFFFFFFTFTFFTTFTFFFTTTTFTTTTTFFTTTTTFTFTTFTFFTFFTFFTFFTTTTFFFFFFFFTFFTFFTFTTTTFTTFTTTFFTTTTFFTFTFTTFFTTFTTTTFTFFTTFTTTFTTFTFTFTTTTTFFFTFFFFTTTFTFFFTTTFTTTFFTFTFFFTFFTFTTFTTTTFTTTTFTTTTFFFTFTTTTTFTFFFFFFFTTTFFTTFFFTTFTTFTTFFTFTFFTTFFFFFFTFFTTFTTFTTTFTFFTTFFTFTFTTTFTFFFTFTTFTTFFTFFFTTFTTFFTFFTFTTTTFFFTTTFFFFFFFTFFTFTTTFTTTTFTFTTTTFTFFFTFFTTTTTTTFTFTTTTTFFFFTFTTFFFFTFTTTFTTTFFTFFTFFTFTFTTTTFTFTTFTTFFTFFFTFFTTTTFFTFFFFFTFTFTFTFTTFFTTTTFFTFTTFTTFTTTFTTTTFFTTFFFTFTFFTTFFTFFFTFTTTFTFTFFTTTTFFTFTTTFTTFTTTTFTFFFFFFFTTFFTTFTTFTFFFTTTTFFFTTTTFTTFFTFTFTTTFFFTFTFFFFTFFFTTFFFTTFFFTTFTTTFFTFTTFTTFFFTTTFTFTFTFFTFTTTTFFFFTTFFFTFTFFFFTFFFFFFFFTFFFTTFFTFTTFTTFFFTFFFFFFTFTFFFTTTTFFFFFFFTFTFFFFFTTTFFTFTTFFFTFFFFFFFFTTFTFTTTTTFFFTFTTTTTTFTFTFFFTFFFTTFTFTFFTFTFTFTFTFTFFFTFTFTFTFFTTFFTFFTFTFTTFTFFFTFFTTFFFFTFFTTFTTTTTTFTTFFFTFFTTFFTTTFFTTTFTTTFFTFTFTTTTTFFFFFTTFTTTFFFFFFTTTTTFFTTFTFFTTTFTFFTTFTTTFTFFFFFTTTFTFTTTFTFFTFTTFFFFTFTTTFFFTFFTTTTFTTTTFTTFFTFFTTFTFTTFFFFTTFTTTFFFFFFTFTFTFFFTTFFTTFFTTFTFFTFFTTFFTTTTTFFTFTTFTTFFTFTFTFFFTFTTFFTFFTFFTFFTTTFFTFTTFFFFFFTFTTTTFTTTFTFTFFFTFTFTFTFTTFFFTTFFTFTTFFFFFFFTTTTFFFFTTTFFTFTTFTFTFTTTTTTFFFFFFTTFTTTTTTTFFTTTFTTFTFTFFTFFTTFFFTFTTFTFFFFFFFTFFTFFTFFTFTTFFFFFTTFFTFTTTFFFTFFFTTTFFFTFFTTFTFTTTFTTTFTTFTFTFFTFFFTFFTTTFFTTTFTFFTFFTTTFFFTFFFFFTTTTFFTTTFTTTFTFTFFTFTTTTFFTTFTTFFTFTTTTTTFTTTTTTFTFTFTFFTFTTFTTFTTFTTTTFFFTTFTFFTFFTTFTTFTFFTFFFTTFTTTTTFFFTFFTTTFTFTTTFTFFFTFTTFTTTFFTFFTTFTTTTTFFTTFFFFFTFTFTFFFTFTFFFTFFTTTFFTTFTTTTTTFTTTTTFFTFTFFTFTTTTFTTFTFTTTTTTTFTTTFFTFFFTFFTFFTFTTTFFFFTTFFTFTTFTFFTFTTTFTFFTTFFFTFFTTTFTTTFTFFFFFTFTFFFFTFFTFTFFFTTFFTTTTTFTFFTFTTTTTTFFTTTFFTFTFTFFTFTTFTFFTTTFTFTTFTFTTTTTFFTTFTTTTFFFFFTFTFFTFTFFFFFTTTFFTFTTTTTTFFFTFFTFFFFFFFTTFTTFFFTTFTFFTTFTTFFFFFTTFTFTTTFTTFTTFTTTTTFTFTTTFTTFTFFFTFTFTTTFTFTFTTTFTFTFTFTFFTTTFTFTTTFTTFFTTFFFFFTTTFTTTTFTFFTFFFFTFTTFTFFTFTTFFTTFTTFFFFFTFFFFFFFFFTFTTFFTTFFFFTTTFFFFTTTFFTTFFFFTTTTFFTTFTTTFFFTTTFTTFFFTFTTTFTFFFTTFTTTFTFFTFTTTFTTFFTTFFTFTFFTTTFFTTTTFTTTTFFFFTFFFTFTFFFFFTFFTTTFFFTFFTTFTTTTFTFTTFTTFTTTFFFTFFTFFFFTFTFTTTFTTFFTFTTFFFFTTFTTFTTTTFFFFTTFTFTTFFTFTTTTTFFTTTFFTFTFTFTFFFFFTTFFFFTFTFTTTFFTFFFFFTTTTFTTFFTFFFTFFTTTTTTTTTFFFFFTTTTTFFFTFFTFTFFTTFTFFTTTFFTTTTFTFFFTTTFFFTTTFFTFTFTFFTTFTTFTTTTTTFFFFFFFTTFFFFFFFFTFTTFTTTFFTTTTFFTTFFFTFFFTFFFFTTTFFFTTFFTTFFTFTTTFFFTFFFTTTFTTFFFTTFFFFFTFTTTTTTTTFFTTTFFFTFTFFFFFTTFTTTTTTTFFFFFTTFTTTTFFTFFTFTTTTFTTFTTFTTFFTTTFTTTTTFTFFTFTFTFFFFTTFFTTTTFTTFTFFFFTTTTFTTTTFFTTFFTTFTFFTTTFFFFTFTTFTTTFFFTTTTFTFTTFTFFTTFFTFFFFTTFTTFTFFTTTTTFTFFTFFTFTFFFFFTFFTFFFFFFTFTTTFTFFFFFTFFTTFTTTTFFFFTTTTTFTFTFTFTTTFTTTFTFFFTFFTFFTTFTFTFFFTFFTFFTTFTFFTFFFTTFTTTTFTTTFTFFFFFFFTFTTFFFFFFFFFTFFTFTFTTTTTFFFTTFTTFFTTFFTFTFFTFTTTFFTTTFTFFFTTFTTFTFTFFTFTTFFFFTFTTTTFTTFFTFTFTFTTFFFTTTFFFTFTFTTTFFTFFTFFTFFTTFTTFFFFFTFFFTFFFTFFTTTTFTTFTTFFFTTTFTFFFTTFTTTFTFFTTFTFFTFTFTFTTTFFFTTTTFTTTFFFFTFFFTFFTTTFFFFFTFTFTFTTTFFFTTTTFFTTTTTTFTFFFFFFTTFTTTTTFTTFTFFTTFTFTFFTFTTTTTFTFTFFFTTFFFTTTTFTTFFTTFFTFTTFFFTFFFFTFTFFFTFFTFFFTFFFTFTTFTTFFTTFTTFTFFTFTFTTFFFFTFTTTFFTTFTFTTTFTFTTTTFTTTTFFFTFTTFTTTFTFTTFTTFFTFTTTFTTTTTTTTTFTFFTFFFFFTFFFTTFTFTFFTTFTTFTTTTTTFFTTTTTTTFTTTTFFTFTFTTTFFTTFFTTTTFFTTFTTTFFFFFTTFFTFTFFTTFFTFFFFFFTFFFFTFTTFTTTFFFTFFTFTFTFFTFFFTTTTFFFTFFFTFTFTTTTFFTTFFFFFFFFFFFTFTTTTTTFFTTTFFTTTFFTFFFFFFTTFTFTTFFFFFFTFTTFFFTTTFFFTTFFTFTFFTFTFTFTTTTTTTFFFTTFTTFFTTTFFTTFTTTFFFTTTFTFFFFTFTFTTFFFFFTFFFFFFFFFFFFTFTFTFTFFFTTTFFFTTTTTTTFTTFTTFTTTTFFFTTTTFFFFFFTFTFFFTFFFTTTTTFTFFFTTFFFTTFFFTFTTTTFFFFTFTFTFTFFTFFTFTFTFFTFFTTFFTFFFTFFFTTFTFFFFTTTFTTTFTTFFFFTTFTFTTFTFTFTFFTFTTTFFFTTTTFTTFFFTFFFTFTTTFTTTTFFFFFTFTTTTTTTTTTFFFTFTTTTTFTTTFFFTTTFTTFTTFFFTFTTFFFTFTTFTTFTFFTFFTTTFTFFFFFFTFTFTTTFFFFFFFTFFTTFTFTTFTFTFTTFTFTFFTTFFTFFTTFTFFTTFFTFTFFTTFTTFTTFTFTTTFFTTTTTFFFTTFFFFTTFFFFFFTTTTFTFTFFFTTFFFFFTTFTFTTTTFTTFTTFFFFFTFFFFTFTTFTTTFFFTFFFFFFFFTTFFTFFFTTFFFFFTTFFTTFTFTTFFTTTTTTFTTTFTTTTFFFTTFFFFTFTFFTFFTFFFFFFTFTTTFTTTTTFTFTTFTTFFFTFFFTTFTFTFTFFFTTFFTFTFFTTFFTTTTTFFTFFTTTFTFTFTFTTFFFFFTTTFFFTTFTTFTFTFTFFTFFFTTFFFTFFFTFFTFTFTFFTFFFFTFFFFTFTFFTFFFFFFFTTFFFFTFTFTTFFFFFFFTTFFTTFFFFFTFFFFTTTTFTTFTFFFTTFTFFTFFFFTTFTFTTFFTTFTTFFTTFFFFTTFFFTFTFTFFFFTFTFTFFFFTFTFTFTTFFFTTFFTFFTFTTFTFTFFTTTFTFTFTTTFFFFFTFTTTFTFTTTTFFFTTFFTTFTFFTTTTFTTFTTFFFTFTTFFFTFTTFFFTTTTFTTFFFTTFFFTTFFFTFFFTFFTFFFFTFFFTFFTTFFFTTTTTTFFFTTFFTTTTFTFTFFTTFFTTFFTTFFFTTFTFTTTTTTTTTFFFFFTFTTFTTTFFFFFFFTTFFTFFTFTTFTTTTTFTFTTTTFTFTTFFFFFTTFFFTFTFFFTTTTTFFFFFFTFFTFFFFTFTFTFTFFFFFTFFTFFTTTFTTFFFTFTTFFFTTTTFTTFFTFTFFFFFTFFTTFTFTTTFFFFTTTTTFFTTTFTFFTTFFTTFTTFTTTFFFTFTTFTFFFTFTFTFFFFFTTTFTFTFTFTTFTFFTFFFFFTTTFFTFTFFFFFTTFTFFTFFFFTTFTFTFTTTTTFFTFFFTFFFTFTTTFFFTTFFTTTFTTFTTTFFTTFTFFFTFTFFFTTFTFFTTFTTTTTFFTTFFTTTTFTFFFFTTTFTTFTFTTFFTTTTFTTTTTFFFFTFFTFFFTTFFFTTFFFTTTFTFTFFTFTFFTFTFFTFTFFFFTTTTTFTFTFTFTFFTTTTTFTFTTFFFTFTFFTFFFTFTFFTTTTTFTFTFTTTFTTTTTFFFTFTFFFFTFTFTTFFFFFTFFFFTFFFFTFFTFFTTFFFFFFFTFFFTFTFTFTTFTTTTFTTTTFTFFTFTTTFTFTTFTTTTTFTTFFFTTFFFTTTTTTTTFFFFFFFTTTTFTTTFTFFTFTTTFFTTFFTFFTTTTTTTTTFTFFFFFTFTTTTTFTTTTFFTTTFTFTFTTTFTTTTTFFTTFTTTTTFFFTFTTFTFTFFTFTFFTTFFTTFFTFTFFTTFTFTFTFFFFTFTTFFTFTFFFTTTFFTTTFTFTTFFFTFFTTTTTTTFTFFFTFTFTFTFTTTTFTFFFTFTFFFFTFTFFTFTFFFFFTFTTTTFFTFTTFTTFFFTFTTTFTTTFFFTTFTTTTTTFTTFFTTTTTTFFTTTTTTFTTFTFFFFTTFTTFTTTTTTTFTFTFFFFFFTFFTTFTTTTTFTTFTTTTFFTFFFTTFTFFFTFFTFFTFFFTFTFFFFTTFFFFFFFTTTFFTFTFTFFTTFTTFFFFFTTTFFTTTTTFTTTFFTFTTTTTFTFFFFFFFFTTTTFTFTTFFTFFFFFFFFFFTTTFFFFFFFFTTTTTTTTFFTFTFTTTFFFFFTFTTFFTFFFFTTFFTFFTFFFTTTFTTTTTTTTFFTTTTTTFTFTFFTTFFTTFTTTTTTTFFFTTFTFFFFTTTFTTTTFTFTTFFFTFFFTTTFFTFFTTTFTTTTTFFFTTTTFTFFFTFTFFFTFTTTTTTFFFFTTFFFTFTTTTTFFTFTTFTFFFFFTTTTTTFTFFTTFTTFFTTFFFFTTTFTFTFFFFFFTTFTTTFFFFFTFFTTTFTTTTTTFFTTFTFTTTTTFFFTTFTFTTFTTTTFTTTTFFTTTFTFTTTFFTTTTTTFFFTFFTFFTTTFFFFFFFFTTTFTTTTFFFFFTFFTFFTTTTTTTTTFFFTFFTTFFFTTTTFFTTFTFFTTFTTTTTTTTTTTTFTFTFFTFFFTFTTFTTTTFTTTFTTTTFTFFFTFFTFFTTFTTTTTTFTFFTFFFTFTTTFTFTFTTTTTFTFFTFFFFTFFFFTTFFTFFTTFTFTTFFTTFTTFTTFTFFFFTTTTTFFTFTFTFTTTFTTTFTTTTTTFFFFFFTTFTFFTTFFTFTTTTFFTFFTFTTFTTFFFFTFFFTFFTFTFFTTFFFFFFTFFTFTFTFTTTFTFTFFFFFFTFTFFTTTFFFTTTTTFTTFFTFTFFFTFFFTTTTFTTTFFTTFTTFFTTFFTFTTTTTFTTFFTFTFFTTTFTFTTFTTTTTFTTFTFTTFTFTFTTTTTTTTFFTFTFTTTFFFTTFFTTTFTTTTFFFFTTTTTTTTFFFFTTFTFTFFFTTFFFFFTFFFFFTFTTTFFFTTFFFTTTFTTTFFFFFTTFFFFFFFFTFTTTTFTFFTTTFFTFTTTTFTTFFFTFFFTTFTFTTFTFTFFFTFFTTFTTTFTFTTTFTTFTFFTFTTFFTFFTTFFFFTFTTTFTTFFFTTTTFFTTFFTFFTFTFTFFFTFTTTTFTFFFTFTTTTFTTFFFTFFFFFFFTTTFTTTTTTFFTTTTTFFTTFFTTTFFFFFFTFFTTFTTTTTFTTFFTFTTTTTFTFTFFFTTTTFFFTFFTFTFFFFTTFFFFTFFTFFTTFFTTTTFTTFTTFTFFFTTFFFTFFTFTFTTFTTTFTFTFTFFFFTFFTTFFTFFFTFFTFTTTTFFTFFFFTFTFFFTFFFTTFFFTTFFTTTTFFTTTTFTFTTTTFTTFFFTFTTFTFFTFTTFFTFTTFTFFFFFTFFFFTTTFTTTTTFTFFFFTFFFFTFTTTTFFFTTTTFTFFFTFTFTFTFTTFTFTTFTTFTFFFFTTFTFTTFFFTFFFFFFFFTFFTTFTFFFTTFTFFFTFFTFTTFTTTFFTTFTFTTFTFTFFFFFFTTFFFTFTTTTFFFTFFFFTTFTTFTFTTFFTTTTTTTTFTFFTFTFFFFFFTFTFTFTTTTFFTFFFFFFFFTFTFFFTTTTTTTTTFTTTFFTFFFTTFFFTFFTFTFTTTTFFFFFTTFFTFTTTTFTTFTTFTTTFTTFFFTFFFFTFTTFTTTTFFFTFTFTFTFFTFTTFTFTFTFFFFFFFFFFFTTTTFFTFFFFFFTTFFTTTFFFFTFTFTTFFFFFFTTTTFFTTFTTTFTFTTTTTFTTTFTFTTTTFFFFTFTTFFFTFTFTTTFTTFTFTTTTTTFFTTTFTFFTTTFFTFTFTFTFFFFTTFFTFTFFFFTFFFFTFFFTFFTFTTFTTTTFTTTFFTTTTFTTTFTFTTFFTFFFFTFFTFTTFTTTTTTTFTTFFTTFFTTTTFFTFTFTFTFFTFTTFTFTFFFTFTTTTTFTTFTFFTFTFTTFFTFFTTTTTTTFTFFFTFTTTTFFFFFFFTFTFTFFFFFFTTFFFFFFTTTFFTTTFTFTFFTFFTTTFTTFFFTTTTFFTFFFTFTTTTFTTFFFFFTTTTTTFFFFTTTTTTTFFTTTFFTTTTTFTFFTFFTTTTFTTTFFTFFTTFFFTFTTTFTFTTTFTFTFTFFTTTFFTFFTFFTTTFFTTTTFTFTTTFTFTFFFFTTFFTTFTFTTFTTFTTFTFTTTTFFTTTFTTTTFTFTTFFFFFTTTTTTFTTTFFTFTTTFTFTTFTFFFFFFFFFTTFFTFFTTFFFFFFTFTFTTTFFFFFFTTFFFFFTTFFTTFFTFTTTFFFFTFTFFFFTTFTTFTTTFFTTFFTFFTFTFTTFFTTFTTTFTFTFTFFFTFTFFFTFFTFTTTTFFFTTTTFFFTFFTTTFTFFFFFTFTFTFTFFFTTFTTFFTTTFFFFTTTTTFTFTTTTTTFTTTTTTTTTTTFFTTFFTTTTFTTFTTTTFFTFTTTTFFFFTFTFTTFTFTTTFFTFTTFTFTTFTFFFFTFFFTFFTFFFFTTTTTFTFFFTTFFFTTFTTTTTTTTTFFFTTFTTFTFFFTTFTFFFFFTFFFFTTTFTTFFFTFFTFFFTFTFFFTFFFFFFTTFFTFTTTFTFTTTFTFFTTFTFFFFFFTFFFTTTTTFTTTFFFFFTFFTFFFFFFTTTTTFFFTFTTFTTTFTTTFFTFTTFFTFFFTTFFTFFFFTTTTFFTFTTFFFTFTFFFTTFTTFFTTFFTFFFFFTFFTFFTTTFTTFFTTTTFFTFFTTFFFFFFTFTTTTFTFFFFFFTTTTFTTFFTFTTTFTFFFFTTTFFTTFTFTTTFFFFTTFTTTFFFFTFTTTFFFTFFTFFTFFFTFFTTTFFTFFFFTFTFTFTFTFTFTTTFTFFTFTTFTTTTTFFTFFFFFTTFFFTFTFFFTFFFTFFFFTFFTFFTTTTFTTFTTTFTFFFFTTTFTTTFTFTTTFTTTFTFFFTTTFFFTFTFTFFFFTFFFFFTFFTFTTFFFTFTTFFTFFTTFTTTFFTTFFFTTFTTFTTTTFFFTTFFFTFTTTFTFFFFTTFTFTFTTTFFTTTTTTTTFTTFFFTTTFFTFTTFTTFFTFTTTTFFFTTFTFTFTTFTTTTFFFTTFFTTTFTFFTTFFTTTFTFFFTFFFFFFTFTFTFFFTTFFFFTFFTTFFTTTTTFTTTFTFTFTTFFTTTFTFTFFTFFFFTTTTFTTTTFTTTTFFTTTTFFTFTFFTTTTFTFTTFFFFTFFTTFFTFFTFTTFTFFFFFTFFFFFFFTFFFFTFTTFTFFTTTTFFFTFTFFTTFTFTFTFTFFFTTTFFTFFFFFTTFFTFFFFFFTFFTTTFTTFTFTFTFFTFFFFFFFFTTFTTFTFFFFTFFTTTFFFTFTTTTFFFFTFFTTTFTFFTTFFFTTTFFTTTTTTTFFFFTFTTTFFTFTFFTTTTTTFFTTFTFTFTFFTTTFTTTFTFFFFTFFTTFFFTTTTFFFTFTTTTTTFTFTFFFFTTTTTFFTFFFTFFTFFTTTTTFFFFFTFFFFFFFTTFFFTTFTTFFFFFFFFFTFFTFTTTTTFTTFTTTFFTFFTFTFTFFTFFFTFTTTFTFTFFFTTTFFFFFTTFTTFTTTTFTFFTTFTTTTFTTTTTFFFTFFFTTFFFTTFFFTFFFFTTTFTTFTTFTFFTFTTFFTTFFTTTFTFTFFFFTTFFTTFTTFFTFTFFFTFFFTTTTFFTFTFTFFTFFFTFFFFTFFFTTFFTTFFTFFTTTTFFFFFFTFFTTFFTTTTTFTFTTTFFFTTFFFTFFFFTTFFFFTTFTFFFTFTTTTFTFTTTTTFFTFFFTFFTTFFFFTFTTTTFFTTFTTTTFTFTFTFTFTFTFTFFTFTFTFFTFFTTFTTFTFFTFTTFFFFTFTFTTFFTTFTTFFFFFFFFFTFFTFTFTFTTFFTFFTTTTFTTFFFFFTFTFTFTTTFFTTTFTTFTFTFTTTFFTTTTFFTFTFTTTTTFFTFTTTFFTFTFTTFFFFFFTFFTFTTTTTTTTFTTTTFFTTFFFTTTFTTFFFTTFFTTFTFFFFTFTFFFTFTFFTTTTFTFTFFFFFFTFTFTTTFFFTTTFFFTTTTTFFFTFFTFFFTFTTFTFFFFFFTFTTFTFFFTTFFTTTFTFTTFFFFTTFTFFFTTTFTTTFTTTFFTFTTFTTFFTFFFFTFTTTTFFTFTFTFTFFFFFFFTFTFFFTTFFFTTFFTTFFFTTTTFTFFFTTFTTFTFTFFFTFFTTTTTTTTTTFFTTTFFFTTTFTFTFFTTTTTFTFTTFFTFFTTFFFTTFFFFTFFTTTFTTTTTFTTTTTFFFFFTFFTTTFTTTTTFFFTFFTTFTFFFFTTFTFTFTTFTFFFTFTFFTTTFFFTFFTTTTTTTTTFTFTFFFTFTFTTTFFTTTTTFTFFTTTTFTTTTFTTTTTTTTTTFFTTTFFFTTFFFTTTFFFTFTTFFFFTFTTTFTTFFFTFTFTTFTFTTTTTTTFTTFTTTTTTTTTFTTFTFTTFFFTTTTFTTTTFTTFFFTFTFFFTTTTFTTTFFTTFTFFFFFFFFFFFTFFFFTTTFFTTTFFTTTTTTTFTFFTTFTTTTTTTTTFTTFTFFTFFTTTTTTTTFFTFTTFTTFFTTFFFFTFTTTFFTTFTFFTTTFFTFFFTTTFTTFTFFFFTFTFTFTTFTTTTTTFFTFTTFFFFTFTTTFFTFFFFFTTTTTTTFFFTTTTTFFFTFTTTTFTTFFFFTFFTTTTTTTTFTFTFTFFTTFFFTTTFFFFFTTTTFFFTTTFFTTTTFFTFFTFFFFTFTTTTFTTFFTFFFFFTTFFTTFTFTFTTTFFTFTTTFTFTFTTFFTFTTTTTFTTTFTTFTTTTTTTFTFTTFFFTTTTTFTTFTFFFTFTTFTFFTTFTTFFFFTFTFTFTFFTTFTTTFTTTTFFFFFTFTFFTFTTTTTFFTFFFTFFFFTTFTTTFTTTTTTFTFTFFTFTTFFTTTFFTFFTTTFFTFTTFTFFFTTFTTTFFFTTFFFTFTTFTTFTTFTTFFFTFTFFTTTFTTTFTTTTTTTTTFTTTFTFTTFTTFFFFTTFTFTFTFTFFTFFFFFTTTTTFFTFTTFTTFTFFTFFTFTTFTTTFFFFFTTFFTFFTTTTTTFTFFFTFFFFTTFFTFTFFFTTTTTFFTFFFTTFFTTFTTFFFFTTTTTFTTTFTTTTFFTFFTFFTTFTFTTTFTTFTFFFFTFFFTFFTFFTTTFTFTFTTTTFFFTTFTTFFTFFFFFFFTFFFFTFFTTTTFFFFTFFTTTFTFTTFTTFFTTTFTFFTTTTTTTFTTTTTTFFTTTFFTTFFTFTTFTTFFFFTFFFTTFFFTTFFTFFTFFFTTFFFTTTTFTFTFFTFFTFTFTFFTTFTTFFTTFFFFFFFTFFFTTTFFTTFTFTTFTTTFFTFFFFTFFFFTFTTTTFTTFTTFFTFFFTTFTTTFFTFFFFTFTFTFTTFFTFFFFFFTFTFTFTTTTTFTFTTFTFFFTFFFTTFFTFTFTTFTTFTTFTFFTTTFFFFTTTTTTTFFTTTFFFFTFTTFFTFTTTFFTFTFTTFTFFTTTFTTTFFFTTFFTFFTFTTTTFFFTTFFFTFFFTFTTFTFTTFFFTTFFTFFTTFFFFFFTTTFTTTTFTFTFFFTFTFFTTTTTTTFTFTTFTTTTFTTFTTFTTFTFTFFFFTTFTTFFTFTTFTTTTFTFFFFFTTFFFFFTFTFFFTTTFTFTFTFTTTFTTFFFFFTFTTTTFFTTFTFFFTFFTTTFFTFFFFFFTFTTFFTFTTFTFFTFTFFTTFTFTFFFTTFFFTTTFTTFTTTTFFFFTFTFFFFTFFTTTTFFTFFTTFTFFFFTTTFTTFFTTFTTFTFTFFFFFTTFTFTTTTFTTTTFFTFTTFTFFTFFFTFFTTTTFFTTFFTFTFFFFFTTTFTTFTTTFFFTFTTTFFTTFTFTTFTFFFTTTFTTTFFFTFFFTTTFFFTFTTTFFFTTTTFFFTFTFFFTTTFFFFFFTFTTFTTFFFFFFTFFFFFFTFTFFTTTTFTFFFFTFFFTFTTFTTFFTTTFFTFTTFFTFTFTFTTFTTFTTTFTFTTTTTTFTFFFTFTTFTTTFTTTFFFTFTFTFTFFTTTTTFTTTTTFTFTTTTFFTTTFFTFFTTTTFFTTTTFFFTFTTFTFFFTFTTFFTFFTTTFFFTFTTTTFTFTFFFTTTFTFFTFTFTFFFFFTTFFFTFFTTTFFFFTFFTFFTFTFFTFFFFTFFFTTFTTFFFTFTFTFTTTTTTTTTFTFFFTTTTTTFFFFTTTFFTTFTTFTTTTFTFFFTFTTTTTTFFFFTFTTTFTFFFTTTTFTFFFTTFFFTTTFTTTFTFFFTFTTTFTTFFTTTTTTFFTFTFFTFTTTFTFFFTFTTFFTTTFFFFFTTTFTFTTTFTFFTTFTTFTTTTTFTFFTTTTTTTTFFFFFTTTFFFTFTFTTTTFTTTTFTTTFFFFFTTFFTFFTFTTTTTFTFTFTTTTFTTFFTFFTTFTFFTFTTFTFFTFTTTTTFFFTFFTFTFFFTFFFFFFFTFFFFFFFTTTFFFFTTTTFFTTFTFTFTFTTFTFFFTFTTTTFFTFTTFFFFTFFFTFFTFTFTFFTTFFFTFTFTFTFFFFFTTTTTTFFTFFTTTFFFTFTTTTFTFFTTFTFTFFFTFTFFFTTFTTFFFTTFFFFTFFFFFTTTTFTTTFFTTTFTFFFFTTTTTFTTFFFTTTTFFTTTTFTTTFFFFTTFFFFTTTTTFFTFTFFFFFTTTTFTFFFFTFFFTFTFTFTFTTFFFFFFTTFTFFFFTTFFFTFFTFFTTTTTTTTTTFFTTTFFTFTFTFFFFFTFTTFFFTTFTTFTFFTFFTFFTFFTFFTFTFFFFFFTTTFFFFFTTFFFTTFTTFFTFFTTTTFTTTFTFTTFFTFTTTTFFTTTFTTFFFTFTFFTFTFTTTTFFFFTTTFFTTFFFTFFTTFFTFTFTFTFFTFFFTFTTTTTTTFTFFTTTTTTFFFTTTTTTTFTFFFFTTFFFFFFFTFFTFTTFTFTFTTTFFTTFFFTFTTFTTFFFTTFFFFFFTFFFFFTFFTTTFFTTTTFFTFTTFTFTFTFTTFTTTFTFTTTFFFFFTFFTTTTTTTTFTTTTFFFFFTFFFTTTFFTFFTTTFTTFTFFFFTFFTTTFTTFTTTTTTFTFFFTTTTTFTTTFTTFTFFTTFFFTTFFTFFTTTTTFTFFTFTFFFTTTFTTFFTFFFFFTTTFTTTTTFFFFTFTFFFTFFTFFTFTFTFTFTTFTFTTFFTTTTFTTFFTFFFTTTTTFFTFTFFFFTFTFTFFFTFFFFTTTTFTFTFTTTTFFTTFFTFTFTFFFTFFTTFFFFFFTFFFFFTTFFFFFTTTFTFFTFFFFTFTTFTFTTTTTTFTTFTFTTTTFTFFFFTTFFTFFFTTFTTTTTFTFTTTFFTFTFTFTTTFFFTTTTTTTTTFFTFTFTTFFTFTTTFFTFFTFTFTTTFFFTFTTFFTTTTTFFTTFFFFTTFFFFFFTTFTFTTTFTTTTTFTTTFTFTTFTFFTFTTFTTFFTTFTTFFTFFFFFTTFFTFTTFTFFTFTFFFTTTTTFTFTTTTFTFTTTTTFFTTTFFFFTFTTFFFTTFFTTFFFFFFFFTTTFTFTFFTFTFTFFTTTTTTTTTFTTTTFTTTTFTFFFTTFTTFTFTTTFFFFTTFTTFTFFFTTTFTTTTTTTFFTTTFTFFTFFFFTTTFTTTFTFTTTTTFFTTFFFFTFFFFFTFFFTTTTFFFTFFTTFTTTTFFFFFFFFFTTFFTFFTTFTFFFTTTFTFTTFTTTFFFTTTTFTTTTTFTFFTTFTTTTTFFFTFFFFTTFFTTFTTFFTFFTFFFFTTFTFTTFFTTTTTFFTFFFTTTTFTTTTFFFTFTFTFFTTFTFFTFFTTTFTTFTFFTFTFTFTTTFFFFFFTTFFFFTFFTTFFTTTTFFFFFFFFFTTFTTFFTTTTFFFTTTTFFFTTFTTTTTFTFTFTFFTFFFTFTTFFTFTFFFTTTFFFFFFFTTTFFFFFTFTTTFTFFTTTTFTTTFTTTFFTTTFFTFTFFFFTTTFTTFTFTTTFTTTFFFTFTFTFTTFTTFTFFTTTTFFFTTTTTTFFFTFTTFFTTFTFFTTTTFTFTTFTTFFTFTTTFFFFTTFFTTTTFFTFFTFTTTTFFTTTFFTTTFFFFFFTFTFTTFTFTFTTTTFFFFFTTTFTTFFFFTFFFTFTFFTFTTTTTTTTTFFTFTFTTFFFTFTTTTTFTTTFTTTFTTTTFFFTFTTTTTFFFFTTFFFTTTTTFTTTFTFTTTTFFFFTTFTTTFFFFFFFTFFTFTFFTTTFFFTFTFTFFTFTTFFFTFFTFTTFFTFTFFTTTTFTTFFTTFTTFTFTFTTTFTTTTTTTFFTTFFTFTTTFTFFTFFTTFTTTTFFFFFFTTFFFFTFTTTTTTTFFTTTFTFTFFTFFTTTTFTTTFTTFTTFFFFTTTFTFFTFTFTTFTFTTFFFFFTFTTFTTTFFTTTTFFTFFTTTFTFTTFTTTTTFFFTFTFTTFTFFTFTTTFTFTTTTFFFFTFTTTFTFTTFTFFFTTFFFTFTTFTTTFFFTFTTFFTFFFTTTFFTFFTTTFTFFTFTFTTTTTFFFFTTTFFFFTTFTFTFTTFTFFFTFTFTTFFTFFFTFTFTFTTTTTTTFFFFFFFTTTTTTFTFTFTTFFTFTFFTFFTTFFTTFFFTFTTTTTTFFTFFTFFFFFFFTFFFFFFFFFTTFTTFFTTTFFFTTFFTFFFFFTFFFTTTFTTFTTFFFFTTTFFTFTFTFTTTTFFTTFFFFTFFFFTTFTFTFFTTTFTFFTTTTTTTFFFTFFTTFFFTTTFFTTFFTTTTTTFFTFTTTFFFFFFFTTTTFFTFFTFFFFFTFTTFFFTFTTFTTTFFFTFFFFTFFTFFFFTFFFFFTFFTTTFFTFTTFTTFFFTTTFFTFFFFTFFFTTTFFFTFFTTTTTFTTTFTFTTFTTFFFFFTTTFFFFFTFFFTTTFTTFTTTFTTTFTTTTTFTFFTTFFTFFTFFFTFTFTFTTTFFFTFFFTFTFTTTFTFFTTFFTFFFFTFFFFTFFTTFTTTTTTFFFFTTTFFFFTTTTTTFTFTTTTTFFFTTFTTTFTTTTFFFTTTTFFFFFFTTTFTFTFTFTFTTTFTFFTFTTFTFFTFTFTTTFTFFFTTFTTFFTTFTTTFFFFTTFFTFFTTFFTFFTTFTFFFFTFTTTTFTTTFTFTFFFTTFFFFFFTFFFTTFFTFFTTTTFFTTFTTTFTTTFFTTTTFFTTFFTTTFFFFFFFTTTTTTTTTTFTFTTFFTFFFFFFFTTTTFFTTFFTFFFTFTTFTFTTTFTFFTTTTFTFFFFFFFFTTTTFTTTFFFTTFTTTFFFFFTTTTTTFTFTTFTTTTTFTTTFFTTTFFFTTTTFFFFTFTTFTTFFFFFTFFTTFFTFTTTTFTFFTTTTFFTTTFTFFFFTTTTTTFTTTFTFTTFTFTTTTFFTTTFFTTTTTTFFFTFTTFFFTTTFTFTFTFFFTTTFFFFTTTTTTTTFTFTFTFTTFFTFTFFTFTTFTFTTTFFFFTFTFFFTTFFTFFTFTFFFFFTFTTTFFFFTTTTFFFTFFFFTFFTTTTFTFTTTFFFFTTFFFTTTFTTFFTTTFFFFFTTFTFTFFFTFFTFFTTFFFFTTFTTTTFTTFFTFFTTFFTFFFTFTFFFTFFFTFFTFFTFTFFFTFFTTFTTFFFFTTTTTFTFTFTFFFTTFTTFTTFTFFFTTTTTTTTFTFTFFFFFTTTTFTFTTTTFFFTFFFTTTFFFFTTFFFTFTTTFTFTTTTTTFFFTFFTFFFFTTTFFTTTFFTFFFTTTTFFFFTFFTTTTTFFFTTTTTFFTFTTTTTFFFFTFFFFFTFTTTFTTTTTFTTFTFFTTFTFFFTFTFFFFTTTTTTTFTTFTFTTTTTTTFTFFTTFTTFTTFFTTFFFTFTFTTFTTFTFFFTFFTTTTFFTFTFFFTTFFTTTTFFTFFFTFFFFFFTFFTFTTFTFTFTTTFTTFTFTFFTFTTTFTFFTFFTTFFFTFFFTTTTFTTFFFTFFTTFFTTFFFFFFTFTTFTTTTFFFFTFFFFTFTFFTFTFTTFTFFFFTFTTTTFTTTTTFFFTFFFFTFTFTFFTTFFFTFTFFFTFFFFTFTFTTTTTTFFTFTTTTFTTFTTFFTTFFTTTTFTTFFFTFTTTFFFTTTFFTFFFFFFFTFTFTTFFTTTTTFFTTTFFFTFFFFTFFFTFTTTTTTFTFTTTFFTTTTTTFTFTTFTFFTFTTTFFTFTFFFFTFTFTTTFTFTFTFFFFTTTFFFTTTTFTFTFTFTTFFTFTTTFTTTTTFFFFTFTTFTFTTTTTTTTFFFFFFFFFFTTFTTTFFFFFFTFFTTTTTTTFTTTFFFTTTTFTTTTTTFFFFFFTTFTFTTFTFTFTFTFFFTTTTTTFFTTFTTFFTTFTTFTFTFTTFTFTFFFTTTFFTFFTFFTFFFFFFFFFFTTFFTFFTTFTTTTFFFFTFFTFTFTTFTTTTFTFTTTTTFTFFTTTFTTFTFFFTTFFFTFFFTFTTFFTFFTTFFTFTTTFTTTFTFFFFFTFFFTTFTTTTFFFTTFFFFTTFFFFFFFTFTTFFFFTFTTFFFTFTTTTTFFFFTTFTTFFTTTFTTTTFTTFFTFFFTTFTFFFTFFFTFTTFTFTTFFFFFTFFTTFTTTFTTFFFFFFTTFFTFFFTTFTFTTFTTTFTTTTTFTTFTFTTTTTTTFTFTTFTTTTTTTTTTTTTFTFFTFFFFFTFFTTFFTTFTFFFTFTTTTTTTFFFFTFFTTTFFFFTFTFFFFTFTTTTTFTFTTTFFTTFFFFFTTFTTTTFFTTFFFFFTTFFFTFTFFFTTFTFFFTTTTFFTTFTTFFFFFTFFFTTFFFTFTFTTFTFTTTTTTFTTTTFTTFFFFTFFFFTTFFTTTTFFFFFFFTFTTFFTTTFTTFFTTFTTTFFTFTFTFTTFTTTFFTTFTTFFTTTTTTTTFTFFFFTTFTFFFTFTFFFTFFFFFTFTTFFTFTFTTTFFFFFTFTFTFFFFTFTTFTFFTTTTTTTTTFFFFTTFTTTTFTFFFFTTTFFFTFTFTTFFTFTTFFTTTFFFTTTFTTTFFFFFFTFFFTFTFTFTFFFTTTFTTFTFTTFFFFTTTTFTFFTTTTFTFTFFFTFFFFFTTFTFFFFTTFTFFTTTTFTFTFFTTFFTFTFFFFTFTTTFTFFTTFFFTTTTFFFFTFFFTFTFTTFFFTFFTFFFTFFFFTFFFFFTTTFFFTTTFFFTTTTTTFTTFTFTFFTFTFFTTTTTFFFFTTTTTTTFFTTFTTTTFFFTFTTFTTTFTTTFTTTTTTTFFTFFTTFTFTFFFFTFTTFFTTTFTTTFFTFFTTFFFFFTTTFFFTTTTFFTFTTTTTTTTTTFFFTFTFTFTTFFTTFTTTTFTFTFTFTFTTTTFFFFTTFTFTFTTTTTFFFTTFFFFTTFTFFTTFTFFTFTFFTFFTTTTTFTTFTFTTTFFTTFFFTTTTFFFTFTTTTTFTFTTFFTTFFTFTFTTTFFTTFTTFTTFTTFFTFFTTFFTFFFFTFTTFFTFTTFFFFTFFFTFFFFFTTTTTFFTFFFFTFFTTFFFFTTTTFFFTTTTTTTTTFFFTFFFTFFTTTFFFTTTFTTFTTFTFTTTTTFFFFFTFTTFTTTFTFFFFFFTFTFTFFFTTTTTFFFFFFTTTTTFFFTTTFTFTTTFFTFFFTFTTFFFTTTFTFTTFFFTFFTTTTTTFTTTFFTFFTFTFTFTFFFFFFFTFTTFFFTFFTFTTFTTTTFFTTFTFTFFFFTFTTFFTTFTTTTFTFTFFTTFTTTTFTTFTFFFFTTTFTTFTTFFTTFFTFTFFTFTTFTFFFFFFFTTFFFFTTFFTTTFFFFFTFTTTFFTFTTTTTTFTTFTFFFTFTFTTTFTFTFTTTFFFFTFFFFTTTTTFFTFFTTTTFFTFFFFFFTFFTFFTFFTTFFTFTFTFTTFTTFTFFTTTTFTTFTTFFFTTTTFTTTFFTFFFFFFFFFFTTFFFTTTFFFTTTFTTTFTTFTTTFTTFFFFTFTTFFFTTTTTFTFTFTFTTFTTFTFFFFFFFFTFTFTFFFTTTTTFFFFFTTFTTFFFFFTTTFTFTFTFTFTFFTFTFFFTFTFTFFTTFFTTTTFFFFFFFTTFTFFTTTFTTTFTTFTTFTTTFTFFFFTTTTFFFFTFFTTTFFTFFFTTTTFFTFTTFTFFTFFFTFFFTFTTTFFTTFTTFTFTFTTTTFFFFFTFTFTTTFFFFTFTFTFTTTFTFFFFFFFTFFTTTFTFFFFFTTTTTFFFFFTFFTTFFTFFTTTTTTTTTTFTFTFTTFFFTFTTTTTFFTFTTFFFTTFTTFTFFFFTFFTFTFFFFTFTFFFFTFTFFTTFFTTTFTFTTFTTFTTTTTFTFFFFFTTFTFFTTTTFTTTTTTTTFTFTFTFTTTTTFTTFFFTTTTTFTFFFFFTFTFTFFFTTFTTFFFTTFTTTFTTFFFFFFFTTTTTFFFFTTTFFFFTTFFTTTTTFFTTFFTFFTTTFFFTTTTFFTTFTTFTFTTTTTTTFTTTTFFFTFTFFFFFTFTFFFFTFTFTTFTFTFFTTFTTFFFFFFTTFTTFTTTFTFFTTTTFFFFFFTFTFFTTFTTTTTFTTFFFTTTTTFFFTTFTFTFFFTFFFTFTTFTTFFFTFFTFFFTTTTTTTFTTTFFTFFFTTTTTTTFTFFTFFTFTTFFTTTFFFFFTTTTTFFFTTFFFFFTFTTFFTFFFFFFTFFFFTFTTFFFFFTTTTTFFTTTTTFTFTFFFFFFTTTFTFFFTFTFFFFTTTTTTFTFTTFTFTTFFFTTTFFFTTFFFTTTTTFFFTFFFFTTFTTTTFFFFTFFTFTFFFTTTFFTFTTTFFFFTFFFFTFFTFTTFTFFFFFFTTFTFFFTTTFFTTFTFFFFTFFTTFTFFTFTTFFFTFTTTTFFTTFFFTFFFTTTTFTFFFFFTTFFTFTTFFFTFFTTTFFFTFFFFTTTTTTFFTTTTFFFTFFTTTTFTFTFTTTFFFTFTFFTTTTFFFFFFTFTFFFTFTTFFTTFFTFFFFTTFFFFTFTTTFFFFTFTFTTFTFFFFTTTTTTFTTFTFTFFFTFFTFTTTFFTTTTTTTFTFTTFTFFFFTFFFFFTFFFTTFTTTFFFTTTFTFFTTFFFTTFTTTTTFFFTFFTFFTTFTFTFTTTFFFTFFFTFFFTTFTTTTFFFFFFTFTFFTTFFTTTFTFTFTFFTFTTTTFTFTTTFFFFTFTFFTTFTFFTTTTFFFTFFFFTTFFTTFFTTTTTFFFFFTFFTFFTTFFTFTFTTTFFTFTFTFTTFTTTTTFTTTFTFFFFTTTTFFFTTFFFTFFTTFTFFFTFFFTFTFFTTTTTFFFFFFFFFFTTFFTTTTTFTFFTTFFFTTFTTFTTTFFFTFFTFTFTTTTFTTTFTTTFTFFTFTFFTFTFTTFFFTFFTFTTFTTFTTFFFFTFTTTTFFFTTFFFFFTTTFFFTFFTTTFFFFFFFFFFFTFTTFFFFTTFTFFTFTTTFTFTFFTFFFTTFFTFFFFFTFTTFFTTTFFFFFFFTTFTFTFTFTTFTFFFTFTFTTTFFTFFTTFTFTFFTFFFFFFFFTFFFTFTFFFTFTTTTTFFFTTFTFTTTTFTFTFTFTTTFFFTFFFFTFFFFFFFTFFFTFTTTFTTTTFFFTFTTTTTFTTTTFTFFFFTTFFFTFTTTFTFTFFFTTFTFFFTTFFTFTFTTTFTFTTFFFTTTTTTTTTFTTFFFTFTFTTFTFTTFFTTTFTTTFTTFFTTTTFFTTTFFFFFTTTTTTTTTFFTFFFFTFFTTTFTTFTTTFTTFTFFTTTTTTTFFFFTFTTFTTTFTFTTTTTFFTTFTFFTFTTFTTTFTTTFTTTFFTFTFFTFFFFFTFTFFTFTFTTTFTFFFTTFFFFTFFTFFTFTTTFFTFFFTTFFFFTTFFTFTTFTFTFFTFTTTTTFFFTFFFFFFTTFTTTTFTTTTTTTTTFTTFTFFTTFFFTTFFFFTFFTFFFTTFTTTFTFFTFFFTFTFTTFTTTTFTTFTTTTTFFTTTTFFFTTTFFTTFFFFTTFTFFFTFFFTTTTFTFTTTTTFFFFTTFFFFFFTTTFFTTFFTTTFTFFFFFTFTTTTFTFFFTFTFTTFFTFTFTFFTTFTTFFTFTTTFFTTTTTTFTTTTFTTTTFTTTFFTTFFFFFTFFFFFTFTFTTFTTFTFFTFTFFTTTTTFFTFFTFTTTFTTTFTFFTTTTTFFTFTFTTTFTTTTTTFFFFTFFFFTTTTFFTTTTFFTFTFTFTFFFTFTFTTFFFTFTFFTFFTTFTFFTFTFFFFTTTFFTFTFTTTFFTFTTFTFFFFTFTFTTFFTTTFFFTTFTTFTFFTTTFFTTFFFTTFFFFTFTTTTFFTFFTTTFFFTFFFTFTFFFFFTFFTFTFTTFFFFFTTTFFFTTTFTTTFFFTTFFTTFTTFTFFTTFTFFTFTTFFFFFFTTTTTTFTFFFTFTFFTTFTFTTTTTTFTFFTFFFFTFTFFTTFTFFFFTTTFFTFTTFTTTFTFFTFTFTTTTTTTTFTFFFFTFTTFTFTFFTFTTTFFFTFFFTTTTTTFTFFFFTFTFTFTTTTFFFFTFFTFTTFTTTFTFTTTFFFTFTTFTFTTTFTTFTTFTTFFFFFFTTFFFTTTTFTTTTTFTFTFTFFFFFTTFTTTTFFTFFFTTFFFTTTFTFTFFFTFTFTTTTFFFTTFTTFFFFTFTFFTTFFFTFFTFTFFTFFTTTTTFTFTFFFTTFFFFTTFFTFTTTFFTTFFFFTFFFFFFTTFFFFFTFFFTFTFTFFFFFTFFTTFTFTFFFTFFTFFTFFFFTFFFFTFFTTTFFTTTFFFFFFTTTTFTTTTTFFFTTTFTTFTFTTFFTTFTTFTFTFFTFFFFFTFTTFFFTTFTTFTFTTTTFTTTFFTFTTFFFTTTFTFFTTTFTTFFFFTFFTFTFFFFFTTFTTTTFTFFFFFTTTTTFFFFFTTTTFFTTFTFFTFTFFFFTTFFTFTTFTTTTTFTFTTTFTFFTFFFFTFFFTFFFTFFTFTTTFFFFTFTTTTFTFFTTTFFTTTFFTTFTFTFTTFTFTFTFTTTTTFTFTTTTFFTTFFFFFFTTFFTTFFTFFTTFFTTTTTTFFFFTTTTFFTFFFFFTFFTTTFTTFFTTTTTFTTFTTTTTTTTTFTTTTFTTTFFFFTFFFFTTFTTFTTTTFFFFFFFTFFFTFTTTTFFFTTTFTTFTTTTFFFFFTTFFFFTFFFTFTTTTTFTTFFTFTTTFTFFFTFFFFTFFFTFTFTTFFTFFTFFTFTTTTTTTFFFFFTFTFTTFFTTFTFFFTFTFFTFFTTFTFTFTFTTTFFFTFTFTFFFTTFTFFFTTTFFTFFTFTTFFFFFTTTFFFFFTTTFFFTTTFFFTTFFTTFFFFTFFFFFFTFFTFFFFTTTTTTFFTFFTTTTTFTTFFTTTTFFFTTTTTFTFFTTFFFFTFFFTFTTTFTFFTTFTFFTTTTFTFTTTTFTTFFFFFFFFFFTTFFTFFFTTFTFTFTFTTTTFTFTFTFTFTTFTTFFTFFTFFFFFFTFFTFTTFTFFFTTTTFFTTFFFTFTTFFFFTTFTFFTTTFFTFFTFTFTFFFFFTTTTFTTFFFTTFTTFTFTTFTTTTFFTTTFTFFTTFTTFTFFFFTTTFTFFTFTFTTTTTFTTTTFFTTFFFFTFTFFFTTTTFTTTTFFTFTTFFTTTFTFFFFFFFTFFFFFTTFTFFFTTFFTTTTTFTTTTFFFFTFTTTTFFTTTFTTTFTFTTTFTTFTFFTTFTTFFTTTFTFFTFFTFTFFFFFFFTTTFTTFFTFTFTFFTFFTFFFTTFTFFTFFFTTTTFFTFFTTFTFTFFTFFTTFTTFFFTTTFTFFFTTTTTFTTTFTFTTTFFTFFTTFTFFTTTTTTFTFFTTFTTFFFTFFFTFFTFFTTFFFTTTFFTFFTTTFFFFTFTTFTFTFFTFTTFTTFTTFTFFFFTFFFTTFFTFFTFTTTTTTTTTTFTFFFFFFTFFFTFFFTFFTTFTTTFFFTFTTFFTFTTTFFFTFTTTTFFTFFTTFTFFTTTTFFFTFFFFTFFFFFFTFTFFTFFTFFTTFFFFFTTFTTFFFFFFFTTTTFTFFFTTFTTTFFTFFTTTFFTTTTTFTFFTTFFTFFFFFFTTTTTTTFFFTTTFFFTTTFFTFFFFFTFTTFFFFFTTTTFTTTTTFTTFTFFFFFFFTTTTTTFFFFTFFTTTTFFTFTFFFTTTFFTTFFTTTFTTFFFFTFTFFFTTTFTFTFTTFTFTFFTFFTFTTTFFFTTTFTTFFFFFTFFTTFFTTFTTTTFFFTFFFFTTTTFTFFTTTFTFFTFFTTTFFTFFTFFFFFFFTTFFTTTFFTTTFTTTFTFTTFFFTTTFTTTTTTTTFFTTFTFTTFTTTFTTFTFTFTTTTTTFFTFTFFFTTTTFTTFFTFTTTTTTFTTTTTTFTTFTFTFTFFFFFFFTTTTTTTTFTFTTFFFFTTFTFFTTFTTTFTTFFFTTFTFTTFFFFFTFTFFFFTTTFTFTFTFTFFTTFTTTFFFFFTFFTFFTFTTTFTTTTFTFFFFFFFTFTFFTTFTFTFTTTTFFTTFFTFFFFTFTFFFTFTFTTTTFTTTFFFTTFTTTTFFTTFFFTFTTTTFTTFFFTTTFFTFFFTTFFFFFTFFTTTTFFFTTFTFTTFFTFTFTFTFTFTFTFFFTTTFTFTFFTTTFFFTTTFTTTTFFFTFTTFFFTTTFTFTTFTFFTTTFTFTTFTTTTFTFTFTTTFFTTFTTTTFFTFTTTFFTFFFFTFTFTTTFFFTFFTFTTFTTTFTFTTTFFTFFFTTFFFTFFFFTTTTTTFTTTTTTTFTTTFTTFFTTTTTTTFTFFTFFFTFTFTTFFTFTFFFFFFTFTTTTTFTTFFFFTFFFTTTFFTFFFTTFTTFFFTTTFTTFTFFTFFFFFTFFTFTTTFTTTTTTTTTFFFFTTFFFTTFFFTTFTTTTFFTTTTTFTFFFFFFTFFTTFFTTFFFFTTTFTTFFTFFTTTFFTTFTFTTTFFFFTFFFTTTFFTTTFTFTTTTTFTTFFTFTTTTTTTTFFFFFTFTTFTFTTFTTFFTFTFFFFTFTFFTTTTTFTFFFFTFFTTFFTTFTFTFTTTFTFFTFTFFTFFFFTTTTFTFTFTTTFTFTTFTFFTFFTFTTFTFTFFFFTTTFFFTTFFFFTFTTTTFTTFFTTFFFFFTTTFTTTTTFTTFFFFFTTTFTTTTFFFTFFTFFFTFTTFFTFFTFTTTTFTTFTTTFTTFTTTTTTTTTFFFFTFTTFTTTFTTTTTFTFFTFTTTTTTFTTTFFTFFTFTFTFFTFFFTTTFTFTTFTFFTFFFFFFTFTTTTFFTTFTFFTTTFFFFFFFFFFTTFFTTTTTTTFTFFTFTFFFTFTTTTFFFTFFFFTFFFTTFTFFTTTTFTTFTFFTTFTFTTTFTTTFFFTTTTFTFTTFTFFTTFTFFFTFTTTTTFFTTTTFFTFFFTTTFTFFFTTFTTTFTTTTFTTFFFTTTTFTFFTFTTTFFTFTFTFFFFFFFTTFTFFFTTFTFTFFTFFTTTFTFFTTTTFFFFFFTFFFTTTFTTFFFTFFFTTFFTFTFTTTFTTFTFFFFFTTTTTFFTTFFTTTTFFTFFFTFFTTFFFFTTTTTFFFFFTFFFFFFTTTFTFTFFFTFTFTFFTTFFTTTFFTFFFFTTTTFTFFFFFTFFTTFFTFTTTFTFFTTTTTTTTFTTTTTFTTFFTFTTTFFFFTTTTFFTFTFTTTFFFFFTFTFFTTFTFTFFFTFTFFTFTFFFTTTTFTFFFFTTFFFFTFTFTFTTTFTFFTTFTTTTFTFTTTTTTFTTFTFTFTFTTFFFFFFFTFFTTFTFTFTFFTFFFFFTFFFTTFFTFTFTTTFTFTTFTTTFFTFFTFFTTTFFTTTFFFFFFTFFTFTTFFTTTTTFTTTTTFFTFTFTTFFFFFTFFFTTFFTTTTFFTFFTTFFFFTFFTTFFTTFFFTTFFFFTFFFTTFFTTTTTTTFTFTTFFTFTTFFTFTFTFTFTTFFTTFFFFFFFFTFFTTFFFTTFTTFFTTFFTFFFFFTFTFFTTFFTTTFTFFFTFTFFTFFTTFFTFFTFTFTTTTFTTFTTTFTFTTFTTTTFFFFFFTTFTFFTFFFFTFFTTFTFFFFTTTFFTTFFTTTFFTTTTTTTFFTFFTFTTTTTFTTTTTFTFTTFTFFTTFTTFTFTFFFFFTFFTFTTTFTFFFFTFTTTFTFFTFTTFFTTFFFTFTTFTFTTTTTTFFFFTTFTFFTFTFFTTFTTFFTTTFFTFFTFFTTFFFTFTFFFFFFTTTTTFTTFTTTFFTFFFTTFTFTTFFFTTFTTFFTFTTTFTTTFFTFFFFFTTFTTTTTTFFTFFFTTFTTTTTFFFTTFFTFFFTTTFTTTFTFFTFFTTTFFFTTTFTFTTTTFFTFTFFTFTTTFTFFFTTTTFFTTFFTFFFTFFFTFFTFTFTFTTFFTFTFTTFFTFTFTFFFTTT"
1825
