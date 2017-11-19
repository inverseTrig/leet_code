# Find Mode in Binary Search Tree

class Solution(object):
	
	def findMode(self, root):
		count = collections.Counter()
	
		if root is None:
			return []
		
		def traverse(self, node):
			if node:
				count[node.val] += 1
				self.traverse(node.left)
				self.traverse(node.right)
			
		traverse(root)
		
		max_count = max(count.itervalues())
		return [k for k, v in count.iteritems() if v == max_count]
