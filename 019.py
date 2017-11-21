# Remove Nth Node From End of List

class Solution(object):
	def removeNthFromEnd(self, head, n):
		index1 = index2 = head
		for _ in range(n):
			index1 = index1.next
		if not index1:
			return head.next
		while index1.next:
			index1 = index1.next
			index2 = index2.next
		index2.next = index2.next.next
		return head
