from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_negative_index, negative_count = -1, 0
        zero_index, max_length = -1, 0

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_count += 1
                if first_negative_index == -1:
                    first_negative_index = i

            if nums[i] == 0:
                first_negative_index, negative_count = -1, 0
                zero_index = i
            else:
                if negative_count % 2 == 0:
                    max_length = max(i - zero_index, max_length)
                else:
                    max_length = max(i - first_negative_index, max_length)

        return max_length

sol = Solution()
print(sol.getMaxLen([1,-2,-3,4]))
