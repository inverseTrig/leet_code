# Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
	if len(s) < 2:
	    return s
	
	n, max_left, max_len, start = len(s), 0, 1, 0
	while start < n and n - start > max_len / 2:
	    left = right = start
	    while right < n - 1 and s[right+1] == s[right]:
		right += 1
	    start = right + 1
	    while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
		right += 1
		left -= 1
	    
	    if max_len < right - left + 1:
		max_left = left
		max_len = right - left + 1
	    
	print(max_left, max_len)
	return s[max_left: max_left+max_len]
