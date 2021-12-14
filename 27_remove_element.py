from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left, right = 0, len(nums) - 1
        k = 0

        while left <= right:
            if nums[left] != val:
                left += 1

            if nums[right] == val:
                right -= 1
                k += 1

            if left <= right and left < len(nums) and right >= 0 \
                    and nums[left] == val and nums[right] != val:
                nums[left] = nums[right]
                right -= 1
                left += 1
                k += 1

        return len(nums) - k


sol = Solution()
print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
print(sol.removeElement(nums=[4, 5], val=5))
