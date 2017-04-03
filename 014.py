# Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
	
	if strs  == []:
	    return ""
	
	LCP = ""
	
        for i in range(0, len(min(strs))):
	    indexChar = min(strs)[i]
	    for j in range(0, len(strs)):
		if indexChar != strs[j][i]:
		    return LCP
	    LCP += indexChar
	    
	return LCP
