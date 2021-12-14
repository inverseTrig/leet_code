from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        digits = []

        def dfs(head, val):
            if not head:
                return

            val = 2 * val + head.val
            if not head.left and not head.right:
                digits.append(val)
                return
            dfs(head.left, val)
            dfs(head.right, val)

        dfs(root, 0)
        return sum(digits)


sol = Solution()
print(sol.sumRootToLeaf(root=[1, 0, 1, 0, 1, 0, 1]))
print(sol.sumRootToLeaf(root=[0]))
print(sol.sumRootToLeaf(root=[1]))
print(sol.sumRootToLeaf(root=[1, 1]))
