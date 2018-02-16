import random
import copy

class Board:
	def __init__(self, n, nums=None):
		"""
		Initializing the board
		"""
		self.x = 0
		self.y = 0
		self.size = n
		self.num = n**2 - 1
		self.board = list()

		# randomly initialize values for the board if nums not provided
		# make sure the board[0][0] is not empty(0)
		if nums == None:
			nums = [i for i in range(n ** 2)]
			random.shuffle(nums)
			if nums[0] == 0:
				nums[0] = nums[-1]
				nums[-1] = 0

		# TODO:
		# 1. check if puzzle is solvable by checking number of inversions
		# 2. change representation of board (2D list) to 1D?

		# copy values to the board and find location of empty space
		for i in range(self.size):
			self.board.append([])
			for j in range(self.size):
				self.board[i].append(nums[i*self.size + j])
				if nums[i*self.size + j] == 0:
					self.x = i
					self.y = j

	def getSize(self):
		return self.size

	def getMaxNum(self):
		return self.num

	def getNum(self, i, j):
		return self.board[i][j]

	def getBoardAsGrid(self):
		return copy.deepcopy(self.board)

	def getBoardAsList(self):
		return [self.board[i][j] for i in range(self.size) for j in range(self.size)]

	def getEmpty(self):
		return self.x, self.y

	def isLegal(self, action):
		if action == 'l' and self.y != 0:
			return True
		elif action == 'r' and self.y != self.size - 1:
			return True
		elif action == 'u' and self.x != 0:
			return True
		elif action == 'd' and self.x != self.size - 1:
			return True
		else:
			return False

	# return a new board that moved the empty location up, down, left or right
	def move(self, action):
		new_board = copy.deepcopy(self)
		if not new_board.isLegal(action):
			print "Illegal move:", action
			return new_board
		i = new_board.x
		j = new_board.y
		if action == 'l':
			new_board.__swap(i,j,i,j-1)
			new_board.y = j-1
		elif action == 'r':
			new_board.__swap(i,j,i,j+1)
			new_board.y = j+1
		elif action == 'u':
			new_board.__swap(i,j,i-1,j)
			new_board.x = i-1
		elif action == 'd':
			new_board.__swap(i,j,i+1,j)
			new_board.x = i+1
		else:
			# should not be in this else statement
			print 'What the heck?'

		# new_board.printBoard()
		return new_board

	def __swap(self, x1,y1, x2, y2):
		tmp = self.board[x1][y1]
		self.board[x1][y1] = self.board[x2][y2]
		self.board[x2][y2] = tmp

	def wins(self):
		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] != i*self.size + j:
					return False
		return True
	
	def isSolvable(self):
		print 'isSolvable() function not implemented yet'

	def __eq__(self, board2):
		if self.x != board2.x or self.y != board2.y or self.size != board2.size or self.num != board2.num:
			return False
		l1 = self.getBoardAsList()
		l2 = board2.getBoardAsList()
		return l1 == l2

	def printBoard(self):
		sep = ('+' + '-' * (2 + len(str(self.num)) )) * self.size + '+'
		for row in self.board:
			print sep
			line = '|'
			for element in row:
				# line += ' ' + str(element) + ' ' * (1 + len(str(self.num)) - len(str(element))) + '|'
				line += ' '
				line += str(element) if element != 0 else ' '
				line += ' ' * (1 + len(str(self.num)) - len(str(element))) + '|'
			print line
		print sep

if __name__ == '__main__':
	"""
		Testing the game
	"""
	# Create and print a sample board
	b1 = Board(3, [1,2,0,3,4,5,6,7,8])
	print 'Sample board'
	b1. printBoard()
	print b1.getBoardAsList()
	print b1.getEmpty()

	# User defined board
	if raw_input('Make a new board? [y/n] ') == 'y':
		size = int(raw_input('Board Size: '))
		if raw_input('Make a random board? [y/n] ') == 'y':
			b1 = Board(size)
		else:
			tiles = []
			while len(tiles) < size**2:
				tiles.append(int(raw_input('Enter Number: ')))
			b1 = Board(size, tiles)
	b1. printBoard()
	print b1.getBoardAsList()
	print b1.getEmpty()

	# Start game
	# Enter r/l/u/d for right/left/up/down
	while True:
		action = raw_input('Enter move (l/r/u/d/q):')
		if action == 'q':
			break
		b1 = b1.move(action)
		if b1.wins():
			print 'You Win!!!'
			break

	print 'exit the game'