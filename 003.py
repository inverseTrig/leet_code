# Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        resulting_string = []
	maxlength = 0
	    
	for i in range(0,len(s)):
	    if s[i] not in resulting_string:
		resulting_string.append(s[i])
		if len(resulting_string) > maxlength:
		    maxlength = len(resulting_string)
	    else:
		newindex = resulting_string.index(s[i]) + 1
		resulting_string = resulting_string[newindex:]
		resulting_string.append(s[i])
	return maxlength
