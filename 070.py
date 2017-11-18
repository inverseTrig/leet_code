# Climbing Stairs

# This problem is like the fibonacci sequence.
# F(n) = F(n-1) + F(n-2) because you can take 1 or 2 steps each time.

class Solution(object):
	def climbStairs(self, n):
		if n == 1:
			return 1
		first = 1
		second = 2
		
		for i in range (3,n+1):
			third = first + second
			first = second
			second = third
		
		return second
