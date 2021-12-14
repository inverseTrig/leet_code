from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self,
                root: Optional[TreeNode],
                targetSum: int
                ) -> List[List[int]]:
        result = []

        def find_path(root: Optional[TreeNode],
                      targetSum: int,
                      combo: List,
                      result: List,
                      ):
            if targetSum < 0:
                return
            if targetSum == 0:
                result.append(combo)
                return

            if root.left:
                find_path(root.left, targetSum - root.val,
                          combo + [root.val], result)
            if root.right:
                find_path(root.right, targetSum - root.val,
                          combo + [root.val], result)

        find_path(root, targetSum, [], result)
        return result
