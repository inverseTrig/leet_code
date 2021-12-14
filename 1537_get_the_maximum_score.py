from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = list(set(nums1).intersection(nums2))
        intersection.sort()
        intersection = [0] + intersection + [0]

        max_score = 0
        for i in range(1, len(intersection)):
            left, right = intersection[i - 1], intersection[i]

            n1_left = nums1.index(left) if left else 0
            n1_right = nums1.index(right) if right else None
            n2_left = nums2.index(left) if left else 0
            n2_right = nums2.index(right) if right else None

            max_score += max(sum(nums1[n1_left:n1_right]),
                             sum(nums2[n2_left:n2_right]))

        return max_score % (10**9 + 7)


sol = Solution()
print(sol.maxSum(nums1=[2, 4, 5, 8, 10], nums2=[4, 6, 8, 9]))
