class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 1
        duplicate_count = 0
        previous_element = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != previous_element:
                duplicate_count = 0
            else:
                duplicate_count += 1
            
            if duplicate_count <= 1:
                nums[write_index] = nums[i]
                previous_element = nums[i]
                write_index += 1
        
        return write_index

