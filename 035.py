# Search Insert Position 
from bisect import bisect_right

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
	if target in nums:
	    return nums.index(target)
	else:
	    attempt = Solution().findGT(nums,target)
	    if attempt is None:
		return len(nums)
	    else:
		return attempt
    
    def findGT(self, nums, target):
	i = bisect_right(nums, target)
	if i != len(nums):
	    return i
