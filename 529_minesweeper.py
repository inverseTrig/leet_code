from typing import List


class Solution:
    def updateBoard(self,
                    board: List[List[str]],
                    click: List[int]
                    ) -> List[List[str]]:
        UNREVEALED_MINE = 'M'
        EMPTY = 'E'
        REVEALED_BLANK = 'B'
        REVEALED_MINE = 'X'

        lenI = len(board)
        lenJ = len(board[0])

        def get_nei(i, j):
            delta_nei = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                         (0, 1), (1, -1), (1, 0), (1, 1)]
            nei = list()
            for di, dj in delta_nei:
                i_able = bool(0 <= i + di < lenI)
                j_able = bool(0 <= j + dj < lenJ)
                if i_able and j_able:
                    nei.append((i + di, j + dj))
            return nei

        def count_mine_nei(i, j):
            count = 0
            for _i, _j in get_nei(i, j):
                if board[_i][_j] == 'M':
                    count += 1
            return count

        def next_move(click: List[int]):
            queue = list()
            queue.append(click)
            while queue:
                i, j = queue.pop()
                if board[i][j] == UNREVEALED_MINE:
                    board[i][j] = REVEALED_MINE
                    return

                nei_mine_count = count_mine_nei(i, j)
                if nei_mine_count:
                    board[i][j] = str(nei_mine_count)
                else:
                    board[i][j] = REVEALED_BLANK

                    for i_nei, j_nei in get_nei(i, j):
                        if board[i_nei][j_nei] == EMPTY:
                            queue.append((i_nei, j_nei))

        next_move(click)
        return board


sol = Solution()
print(sol.updateBoard(board=[["E", "E", "E", "E", "E"],
                             ["E", "E", "M", "E", "E"],
                             ["E", "E", "E", "E", "E"],
                             ["E", "E", "E", "E", "E"]],
                      click=[3, 0]))
print(sol.updateBoard(board=[["B", "1", "E", "1", "B"],
                             ["B", "1", "M", "1", "B"],
                             ["B", "1", "1", "1", "B"],
                             ["B", "B", "B", "B", "B"]],
                      click=[1, 2]))
