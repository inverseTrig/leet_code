class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i, num in enumerate(nums):
            set_bits = bin(i).split('0b')[-1].count('1')
            if set_bits == k:
                total += num
        return total

