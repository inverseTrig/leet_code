from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [True] + [False] * (len(nums) - 1)
        for i in range(len(nums)):
            if can_reach[i]:
                if i + nums[i] + 1 >= len(nums):
                    return True
                can_reach[i:i+nums[i]+1] = [True] * (nums[i] + 1)
        return can_reach[-1]

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_jump = 0
        for i in range(len(nums)):
            if max_jump >= i:
                max_jump = max(i + nums[i], max_jump)
            else:
                break
        return max_jump >= len(nums) - 1

sol = Solution()
print(sol.canJump(nums = [2,2,1,1,4]))
print(sol.canJumpv2(nums = [2,2,1,1,4]))