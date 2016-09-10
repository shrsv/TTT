import pygame

class TTT:

	def __init__(self):
		self.matrix = [["_" for x in range(3)] for y in range(3)]
		self.turn = "O"


	def putO(self, i, j):
		if self.matrix[i][j] == "_" and self.turn == "O":
			self.matrix[i][j] = "O"
			self.checkGameStatus()
			self.turn = "X"
		else:
			print "error"
			exit()
	

	def putX(self, i, j):
		if self.matrix[i][j] == "_" and self.turn == "X":
			self.matrix[i][j] = "X"
			self.checkGameStatus()
			self.turn = "O"
		else:
			print "error"
			exit()


	def checkGameStatus(self):
		no_of_empty_dashes = 0 # used for checking a tie

		# check rows

		for i in range(3):
			first = self.matrix[i][0]

			if first == "_":
				continue

			found_a_win = True
			for j in range(1, 3):
				if self.matrix[i][j] != first:
					found_a_win = False
			if found_a_win:
				print self.matrix[i][j], "won"

		# check columns

		for i in range(3):
			first = self.matrix[0][i]

			if first == "_":
				continue

			found_a_win = True
			for j in range(1, 3):
				if self.matrix[j][i] != first:
					found_a_win = False
			if found_a_win:
				print self.matrix[j][i], "won"

		# check diagonals

		center = self.matrix[1][1]
		if center != "_":
			if (center == self.matrix[0][0] and center == self.matrix[2][2]):
				print center, "won"
			elif (center == self.matrix[0][2] and center == self.matrix[2][0]):
				print center, "won"
	
	def printMatrix(self):
		print
		for i in range(3):
			for j in range(3):
				print self.matrix[i][j], " ",
			print 
			print
		print

	def printResult():
		pass
	
if __name__ == "__main__":
	game = TTT()
	game.putO(0, 0)
	game.putX(2, 1)
	game.putO(1, 0)
	game.putX(2, 2)
	game.putO(2, 0)
	game.printMatrix()
