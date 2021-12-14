from typing import List
from collections import Counter
from math import ceil
from copy import copy


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers = [Counter(each) for each in stickers]
        target = Counter(target)
        ways = []

        def dfs(stk, tgt, used):
            print('-----------------')
            print(f'stk: {stk}')
            print(f'tgt: {tgt}')
            if not tgt:
                print(f'tgt is empty! appending {used}')
                ways.append(used)
                return

            for i, s in enumerate(stk):
                overlap = s & tgt
                required = 0
                new_tgt = copy(tgt)
                if overlap:  # if there is an overlap of letters
                    required = max([ceil(tgt[c]) / count for c,
                                    count in overlap.items()])
                    for c, count in overlap.items():
                        required = max(ceil(tgt[c] / count), required)

                    for _ in range(required):
                        new_tgt -= overlap

                dfs(stk[:i] + stk[i + 1:], new_tgt, used + required)

        dfs(stickers, copy(target), 0)
        print(ways)
        return min(ways) if ways else -1


sol = Solution()
# print(sol.minStickers(
#     stickers=["with", "example", "science"],
#     target="thehat"))
# print(sol.minStickers(stickers=["notice", "possible"], target="basicbasic"))
print(sol.minStickers(stickers=["these", "guess",
                                "about", "garden", "him"], target="atomher"))
