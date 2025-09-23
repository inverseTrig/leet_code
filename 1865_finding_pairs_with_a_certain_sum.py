class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_counter = Counter(nums1)
        self.nums2_counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        value = self.nums2[index]

        self.nums2[index] += val

        self.nums2_counter[value] -= 1
        self.nums2_counter[value + val] += 1

    def count(self, tot: int) -> int:
        total_count_of_pairs = 0
        for item, count in self.nums1_counter.items():
            if item < tot:
                pair = tot - item
                if self.nums2_counter[pair] > 0:
                    total_count_of_pairs += count * self.nums2_counter[pair]
        return total_count_of_pairs
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
