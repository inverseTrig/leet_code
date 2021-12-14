from typing import List


class Solution:
    def construct2DArray(self,
                         original: List[int],
                         m: int,
                         n: int,
                         ) -> List[List[int]]:
        if len(original) != m * n:
            return []

        final = []
        for i in range(m):
            final.append(original[i * n:(i + 1) * n])
        return final


sol = Solution()
print(sol.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
