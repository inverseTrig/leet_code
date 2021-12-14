import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.DEBUG)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seq = [1 for _ in range(n)]

        i_two, i_thr, i_fiv = 0, 0, 0

        for i in range(1, n):
            seq[i] = min(seq[i_two] * 2, min(seq[i_thr] * 3, seq[i_fiv] * 5))
            if seq[i] == seq[i_two] * 2:
                i_two += 1
            if seq[i] == seq[i_thr] * 3:
                i_thr += 1
            if seq[i] == seq[i_fiv] * 5:
                i_fiv += 1

        logging.debug(seq)

        return seq[-1]


sol = Solution()
print(sol.nthUglyNumber(n=27))
