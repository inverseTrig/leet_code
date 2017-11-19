# Maximum Depth of Binary Tree

class Solution(object):
	def maxDepth(self, root):
		if root is None:
			return 0
		elif root.left is None and root.right is None:
			return 1
		else:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
