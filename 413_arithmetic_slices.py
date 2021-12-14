from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        print(diff)
        slices = 0

        count, prev = 0, None
        for d in diff:
            if prev == d:
                count += 1
            else:
                print(f'count: {count}')
                if count >= 2:
                    slices += ((count - 1) / 2) * count
                prev = d
                count = 1
        if count >= 2:
            slices += ((count - 1) / 2) * count
        return int(slices)


sol = Solution()
print(sol.numberOfArithmeticSlices(nums=[1, 2, 3, 4, 1]))
