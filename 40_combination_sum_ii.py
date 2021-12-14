from typing import List


class Solution:
    def combinationSum2(self,
                        candidates: List[int],
                        target: int,
                        ) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.dfs(candidates, target, [], combinations)
        return combinations

    def dfs(self,
            candidates: List[int],
            target: int,
            combo: List[int],
            combinations: List[List[int]]
            ) -> None:
        if target < 0:
            return
        if target == 0:
            if combo not in combinations:
                combinations.append(combo)
            return

        for i in range(0, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates[i + 1:],
                     target - candidates[i],
                     combo + [candidates[i]],
                     combinations,
                     )


sol = Solution()
print(sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
