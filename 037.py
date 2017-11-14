# Sudoku Solver

class Solution(object):
	def solveSudoku(self, board):
		if board == None or len(board) == 0:
			return board
		self.solve(board)
		
	def solve(self, board):
		for i in range (0, len(board)):
			for j in range (0, len(board[0])):
				if board[i][j] == '.':
					for c in range(1, len(board)+1):
						if self.validBoard(board, i, j, str(c)):
							board[i][j] = str(c)
							if self.solve(board):
								return True
							else:
								board[i][j] = '.'
					return False
		return True
	
	def validBoard(self, board, row, col, c):
		for i in range (0, len(board)):
			# Check the whole column to see if there are duplicates
			if board[i][col] != '.' and board[i][col] == c: 
				return False
			# Check the whole row to see if there are duplicates
			if board[row][i] != '.' and board[row][i] == c: 
				return False
			# Check the 3x3 box to see if there are any duplicates
			if board[3 * (row/3) + i/3][3 * (col/3) + i%3] != '.' and board[3 * (row/3) + i/3][3 * (col/3) + i%3] == c: 
				return False
		return True
