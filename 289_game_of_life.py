from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        We will keep 0 and 1 as dead and alive, respectively.
        And we will add 2 and 3 as dead -> alive, and alive -> dead,
        respectively.
        """
        nei = [[-1, -1], [0, -1], [1, -1],
               [-1, 0], [1, 0],
               [-1, 1], [0, 1], [1, 1]]

        def next_interation(board: List[List[int]], i: int, j: int) -> int:
            begin_with = board[i][j]
            count = 0
            for di, dj in nei:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                    count += board[i + di][j + dj] % 2

            if begin_with == 0 and count == 3:
                return 2
            elif begin_with == 1 and (count not in [2, 3]):
                return 3
            return begin_with

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = next_interation(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
