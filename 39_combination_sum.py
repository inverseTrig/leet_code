from typing import List


class Solution:
    def combinationSum(self,
                       candidates: List[int],
                       target: int,
                       ) -> List[List[int]]:
        combinations = []
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
            combinations.append(combo)
            return

        for i in range(len(candidates)):
            self.dfs(candidates[i:],
                     target - candidates[i],
                     combo + [candidates[i]],
                     combinations,
                     )


sol = Solution()
print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(sol.combinationSum(candidates=[2, 3, 5], target=8))
