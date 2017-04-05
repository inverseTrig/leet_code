# Substring with Concatenation of All Words

from collections import Counter
from copy import deepcopy

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
	
	indices = []
	
	total_len = len(s)
	total_words = len(words)
	len_of_word = len(words[0])
	
	counter = Counter(words)
	for i in xrange(len_of_word):
	    temp = deepcopy(counter)
	    index = i
	    
	    for j in xrange(index, total_len - len_of_word + 1, len_of_word):
		word = s[j:j+len_of_word]
		temp[word] -= 1
		
		while temp[word] < 0:
		    temp[s[index:index+len_of_word]] += 1
		    index += len_of_word
		if j + len_of_word - index == total_words * len_of_word:
		    indices.append(index)
		
	return indices
