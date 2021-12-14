import re
import operator
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tk = re.split('(\D)', expression)
        nums = [int(i) for i in tk[::2]]
        ops = map({"+": operator.add,
                   "-": operator.sub,
                   "*": operator.mul,
                   },
                  tk[1::2]
                   )
        for i in ops:
            print(i)

        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]

        return build(0, len(nums) - 1)

sol = Solution()
print(sol.diffWaysToCompute("2*3-4*5"))
