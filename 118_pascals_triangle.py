from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            result.append(list(map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1])))
        return result

sol = Solution()
print(sol.generate(numRows=5))
