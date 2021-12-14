from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(s)}

        mxm = 0
        parts = []
        for i, c in enumerate(s):
            mxm = max(mxm, rightmost[c])

            if mxm == i:
                parts.append(i)

        if not parts:
            return parts

        result = [parts[0] + 1]
        for i in range(1, len(parts)):
            result.append(parts[i] - parts[i - 1])
        return result


sol = Solution()
print(sol.partitionLabels(s="ababcbacadefegdehijhklij"))
print(sol.partitionLabels(s="eccbbbbdec"))
