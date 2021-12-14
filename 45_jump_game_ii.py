from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachable, current_coverage = 0, 0
        last_jump, jumps = 0, 0
        if len(nums) > 1:
            for i in range(len(nums)):
                current_coverage = max(i + nums[i], current_coverage)
                if last_jump == i:
                    last_jump = current_coverage
                    jumps += 1
                    if current_coverage >= len(nums) - 1:
                        return jumps
        return jumps


sol = Solution()
print(sol.jump(nums = [2,500, 1, 1, 1, 11 , 1, 1, 4]))