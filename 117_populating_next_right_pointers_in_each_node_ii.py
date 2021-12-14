"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = tail = Node(0)
        while root:
            for c in (root.left, root.right):
                tail.next = c
                if c:
                    tail = tail.next
            if root.next:
                root = root.next
            else:
                root, tail = head.next, head
        ereturn root