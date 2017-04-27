# Group Anagrams
# This one passes 99/100 and fails because TLE.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == []:
	    return []
	else:
	    strSorted = []
	    strIdx = [None]*len(strs)
	    count = 0
	    grouped = []
	    for i in xrange(0, len(strs)):
		jstr = ''.join(sorted(strs[i]))
		if jstr not in strSorted:
		    strIdx[i] = count
		    grouped.append([])
		    count += 1
		else:
		    strIdx[i] = strIdx[strSorted.index(jstr)]
		strSorted.append(jstr)
		grouped[strIdx[i]].append(strs[i])
		
	    # grouped = [[] for _ in range(max(strIdx)+1)]
	    
	    
	    # for j in xrange(0, len(strs)):
		# grouped[strIdx[j]].append(strs[j])
	    
		
	    return grouped
	    
print(Solution().groupAnagrams(["eat", "te", "aet", "tet"]))
	    
	    
