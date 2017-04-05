# Generate Parentheses

class Solution(object):
    ## This does not generate the ones like a duplicate of each (())(())
    def generateParenthesis(self, n):
	if n == 0:
	    return []
	if n == 1:
	    return ["()"]
	else:
	    nPar = Solution().generateParenthesis(n-1)
	    nHalfPar = Solution().generateParenthesis(n-2)
	    gPar = []
	    for i in xrange(len(nPar)):
		gPar.append( "(" + nPar[i] + ")" )
		gPar.append( "()" + nPar[i] )
		gPar.append( nPar[i] + "()" )
		
	    gPar = list(set(gPar))
	    gPar.sort()
	    
	    return gPar
    
    ## This solution works.
    def genPa(self, n):
	def generate(p, left, right, parens=[]):
	    if left:         generate(p + '(', left-1, right)
	    if right > left: generate(p + ')', left, right-1)
	    if not right:    parens += p,
	    return parens
	return generate('', n, n)

print(Solution().genPa(4))
