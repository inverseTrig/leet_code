from typing import List


class Solution:
    def friendRequests(self,
                       n: int,
                       restrictions: List[List[int]],
                       requests: List[List[int]]
                       ) -> List[bool]:

        def process_request(i: int, j: int) -> bool:
            if i > j:
                i, j = j, i
            if relations[i][j] == 0:
                return False

            for e, each in enumerate(relations[i]):
                if each == 0:
                    relations[e][j] = relations[j][e] = 0

            for r in relations:
                print(r)

            return True

        # 1 for possible, 0 for restricted
        relations = [[1] * n for _ in range(n)]

        for i, j in restrictions:
            relations[i][j] = relations[j][i] = 0

        result = list()
        for i, j in requests:
            print(f'\n\n Request: {i}, {j}')
            result.append(process_request(i, j))

        return result


sol = Solution()
# print(sol.friendRequests(n=3, restrictions=[
#       [0, 1]], requests=[[0, 2], [2, 1]]))

print(sol.friendRequests(
    n=8,
    restrictions=[[6,4],[7,5],[2,6],[1,5],[6,7],[6,5],[0,3],[5,4],[0,4],[2,7],[0,2]],
    requests=[[6,3],[0,2],[0,5],[0,3],[6,4],[2,4],[1,0],[2,1],[2,5],[6,7],[7,0],[3,2],[3,5],[2,1],[1,6],[7,4],[6,3],[1,3],[6,5],[3,7],[7,0],[6,5],[0,5],[0,4],[7,5],[7,0],[7,0],[1,3]]))
