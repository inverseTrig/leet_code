# Rotate List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def rotateRight(self, head, k):
        
        # Check if the list is empty or k = 0
		if head == None or k == 0:
			return head
			
		# Set indices needed to go through the list
		indexA = indexB = head
		length = 1
		
		# Go through the whole list to find the length
		# This is important because k might be larger than the length of the list
		while indexA and indexA.next:
			indexA = indexA.next
			length += 1
		
		# Now that we know the length, we take the mod
		# And also reset the index we used back to head
		k %= length
		indexA = head
		
		# Go through the list with the first index to set the distance from second index
		while k:
			indexA = indexA.next
			k -= 1
		
		# Now we move the indexA to the last one, to connect to the head (in a circle, so to speak)
		# And move indexB to where the list should end
		while indexA and indexA.next:
			indexA = indexA.next
			indexB = indexB.next
		
		# Connect the last item and the head
		# Set the head to be the item after the ending one
		# And cut off the list to be a linear one
		indexA.next = head
		head = indexB.next
		indexB.next = None
		
		return head
