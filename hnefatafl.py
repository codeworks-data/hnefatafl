
from enum import Enum

class HnefataflGame:
	def __init__(self):
		self.board = self.initBoard()
		
		
	def initBoard(self):
		board = [[0]*11 for _ in range(11)]
		
		board[0][3] = Piece.BLACK
		board[0][4] = Piece.BLACK
		board[0][5] = Piece.BLACK
		board[0][6] = Piece.BLACK
		board[0][7] = Piece.BLACK
		board[1][5] = Piece.BLACK
		
		board[3][0] = Piece.BLACK
		board[4][0] = Piece.BLACK
		board[5][0] = Piece.BLACK
		board[6][0] = Piece.BLACK
		board[7][0] = Piece.BLACK
		board[5][1] = Piece.BLACK
		
		board[3][10] = Piece.BLACK
		board[4][10] = Piece.BLACK
		board[5][10] = Piece.BLACK
		board[6][10] = Piece.BLACK
		board[7][10] = Piece.BLACK
		board[5][9] = Piece.BLACK
		
		board[10][3] = Piece.BLACK
		board[10][4] = Piece.BLACK
		board[10][5] = Piece.BLACK
		board[10][6] = Piece.BLACK
		board[10][7] = Piece.BLACK
		board[9][5] = Piece.BLACK
		
		board[3][5] = Piece.WHITE
		
		board[4][4] = Piece.WHITE	
		board[4][5] = Piece.WHITE					
		board[4][6] = Piece.WHITE
			
		board[5][3] = Piece.WHITE
		board[5][4] = Piece.WHITE
		board[5][5] = Piece.KING
		board[5][6] = Piece.WHITE
		board[5][7] = Piece.WHITE
	
		board[6][4] = Piece.WHITE
		board[6][5] = Piece.WHITE		
		board[6][6] = Piece.WHITE
		
		board[7][5] = Piece.WHITE
		
		return board		


	def printBoard(self):
		for i in range(11):
			print(self.board[i])
		

class Piece(Enum):
	BLACK = 1
	WHITE = 2
	KING = 3
	
	
	def __repr__(self):
		if self == Piece.BLACK:
			return "B"
		if self == Piece.WHITE:
			return "W"
		if self == Piece.KING:
			return "K"


def test():
	game = HnefataflGame()
	game.printBoard()
	
test()	