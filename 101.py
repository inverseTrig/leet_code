# Symmetric Tree

class Solution(object):
	def isSymmetric(self, root):
		if root is None:
			return True
		else:
			return self.isSymm(root.left, root.right)
	
	def isSymm(self, left, right):
		if left is None and right is None:
			return True
		elif left is None or right is None:
			return False
		
		if left.val == right.val:
			outside = self.isSymm(left.left, right.right)
			inside = self.isSymm(left.right, right.left)
			return outside and inside
		else:
			return False
