from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ship_count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    left_clear = bool(j - 1 < 0 or board[i][j - 1] != "X")
                    right_clear = bool(i - 1 < 0 or board[i - 1][j] != "X")
                    if left_clear and right_clear:
                        ship_count += 1

        return ship_count


sol = Solution()
print(sol.countBattleships(board=[["X", ".", ".", "X"],
                                  [".", ".", ".", "X"],
                                  [".", ".", ".", "X"]]))
