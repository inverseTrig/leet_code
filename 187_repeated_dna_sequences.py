import re
from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = Counter([s[i:i+10] for i in range(len(s))])
        return [substr for substr, count in counter.items() if count > 1]


sol = Solution()
print(sol.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))