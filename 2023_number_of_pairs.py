from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        combinations = []
        self.dfs(nums, target, [], combinations)
        return len(combinations)

    def dfs(self,
            nums: List[str],
            target: int,
            combo: List[int],
            combinations: List[List[str]],
            ) -> None:
        if target == "":
            if len(combo) == 2:
                combinations.append(combo)
                return

        for i, num in enumerate(nums):
            if target.startswith(num):
                self.dfs(nums[:i] + ['a'] + nums[i + 1:],
                         target[len(num):],
                         combo + [i],
                         combinations,
                         )


sol = Solution()
print(sol.numOfPairs(nums=["7672198", "767", "221", "698566842", "2198903679", "7672198", "2198903679", "76721989036", "973", "767219890367", "2051569", "903679", "605513", "7672",
                           "9", "5", "79", "50", "5657214709160", "673123241121", "3679", "672198903679", "903679", "3651502", "56", "27", "767219890", "198903679", "7", "767"], target="7672198903679"))

# print(sol.numOfPairs(nums=["123", "4", "12", "34"], target="1234"))
# print(sol.numOfPairs(nums=["1", "1", "1"], target="11"))
