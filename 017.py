# Letter Combiations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        list_string = [""]
	
	if digits == "":
	    return []
	
	for i in xrange(len(digits)):
	    
	    if digits[i] == "2":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "a"
		    list_string[sepa+j] += "b"
		    list_string[2*sepa+j] += "c"
		    
	    elif digits[i] == "3":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "d"
		    list_string[sepa+j] += "e"
		    list_string[2*sepa+j] += "f"
		    
	    elif digits[i] == "4":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "g"
		    list_string[sepa+j] += "h"
		    list_string[2*sepa+j] += "i"
		    
	    elif digits[i] == "5":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "j"
		    list_string[sepa+j] += "k"
		    list_string[2*sepa+j] += "l"
		    
	    elif digits[i] == "6":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "m"
		    list_string[sepa+j] += "n"
		    list_string[2*sepa+j] += "o"
		    
	    elif digits[i] == "7":
		list_string *= 4
		sepa = len(list_string)/4
		for j in xrange(sepa):
		    list_string[j] += "p"
		    list_string[sepa+j] += "q"
		    list_string[2*sepa+j] += "r"
		    list_string[3*sepa+j] += "s"
		    
	    elif digits[i] == "8":
		list_string *= 3
		sepa = len(list_string)/3
		for j in xrange(sepa):
		    list_string[j] += "t"
		    list_string[sepa+j] += "u"
		    list_string[2*sepa+j] += "v"
		    
	    elif digits[i] == "9":
		list_string *= 4
		sepa = len(list_string)/4
		for j in xrange(sepa):
		    list_string[j] += "w"
		    list_string[sepa+j] += "x"
		    list_string[2*sepa+j] += "y"
		    list_string[3*sepa+j] += "z"
		
	    else:
		pass
	
	return list_string
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
