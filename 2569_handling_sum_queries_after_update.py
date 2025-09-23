class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        length = len(nums1)
        init = 1<<length

        nums1 = int("".join(map(str, nums1)), 2)

        answer = []
        current_answer = sum(nums2)

        for query in queries:
            action, first, second = query

            match action:
                case 1:
                    a = (init>>first) - 1
                    b = (init>>(second+1)) - 1
                    nums1 = nums1^a^b
                case 2:
                    count_of_ones = nums1.bit_count()
                    current_answer += first * count_of_ones
                case 3:
                    answer.append(current_answer)

        return answer
