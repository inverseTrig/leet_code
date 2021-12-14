from typing import Optional, List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def find_height(node, height):
            if not node:
                return height
            return max(find_height(node.left, height + 1),
                       find_height(node.right, height + 1))

        height = find_height(root, 0)

        result = [[""] * (2 ** height - 1) for _ in range(height)]
        # print(result)

        def write_to_result(node, r, c):
            if not node:
                return

            result[r][c] = node.val
            write_to_result(node.left, r + 1, c - (2 ** (height - r - 2)))
            write_to_result(node.right, r + 1, c + (2 ** (height - r - 2)))

        write_to_result(root, 0, (2 ** height - 1))

        return result
