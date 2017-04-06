# Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
	if Solution().checkVert(board):
	    if Solution().checkHoriz(board):
		if Solution().checkSquare(board):
		    return True
	return False
	
	
	
	
    def checkVert(self, board):
	for i in xrange(9):
	    reset = []
	    for j in xrange(9):
		if board[j][i] != ".":
		    reset.append(board[j][i])
	    if len(reset) != len(set(reset)):
		return False
	return True
	    
    def checkHoriz(self, board):
	for i in xrange(9):
	    reset = []
	    for j in xrange(9):
		if board[i][j] != ".":
		    reset.append(board[i][j])
	    if len(reset) != len(set(reset)):
		return False
	return True
	
    def checkSquare(self, board):
	for i in range(0,9,3):
	    for j in range(0,9,3):
		reset = []
		for x in xrange(3):
		    for y in xrange(3):
			if board[i+x][j+y] != ".":
			    reset.append(board[i+x][j+y])
		if len(reset) != len(set(reset)):
		    return False
	return True
