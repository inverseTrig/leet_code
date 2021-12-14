class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = list()
        for start_i, end_i in firstList:
            for start_j, end_j in secondList:
                if end_i < start_j or start_i > end_j:
                    continue
                if start_j <= end_i and  or start_i <= end_j:
                    lo, hi = max(start_i, start_j), min(end_i, end_j)
                    output.append([lo, hi])
        return output