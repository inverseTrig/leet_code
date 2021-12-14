from typing import List, Optional
from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # def find_height(node, height):
        #     if not node:
        #         return height
        #     return max(find_height(node.left, height + 1),
        #                find_height(node.right, height + 1))

        # height = find_height(root, 0)
        result = []

        def write_level(node, level):
            if not node:
                return

            while level + 1 > len(result):
                result.append(deque())

            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
            write_level(node.left, level + 1)
            write_level(node.right, level + 1)

        write_level(root, 0)

        return result
