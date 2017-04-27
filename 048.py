# Rotate Image

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
	    return []
	else:
	    matrix.reverse()
	    n = len(matrix)
	    for i in xrange(0, n):
		for j in xrange(i+1, n):
		    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	    return matrix
		    
print(Solution().rotate([[1, 2], [3, 4]]))
