# Unique Path

class Solution(object):
	def uniquePaths(self, m, n):
		if m == 1 or n == 1:
			return 1
		
		n -= 1
		m -= 1
		
		if m < n:
			m += n
			n = m - n
			m = m - n
		
		ans = 1
		j = 1
		for i in range (m+1,m+n+1):
			ans *= i
			ans /= j
			j += 1
		
		return ans
