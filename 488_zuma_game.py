from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        @lru_cache(None)
        def dfs(board, hand) -> int:
            if not board:
                return 0

            res = float('inf')
            if not hand:
                return res

            for i, color in enumerate(hand):
                new_hand = hand[:i] + hand[i + 1:]
                for j in range(len(board) + 1):
                    new_board = clear(board[:j] + color + board[j:])
                    res = min(res, 1 + dfs(new_board, new_hand))

            return res

        @lru_cache(None)
        def clear(board: str) -> str:
            stack = []
            for ball in board:
                if stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()

            return ''.join([ball * i for i, ball in stack])

        result = dfs(board, hand)
        return result if result < float('inf') else -1


sol = Solution()
print(sol.findMinStep(board="WWRRBBWW", hand="WRBRW"))
