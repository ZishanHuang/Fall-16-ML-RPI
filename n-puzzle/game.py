import sys
import board

def parseCommand(argv):
	"""
		USAGE:
		-s,  --size <size>				set the size of board
		-d,  --define 					user define the board or not
		-fn, --function <function>		set the function used to solve the game
	"""
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', "--size", dest='size', default=3, help='size of the board')
	parser.add_argument('-d', "--define", dest='define', action='store_true' ,help='user defined board?')
	parser.add_argument('-fn', "--function", dest='fn', default='human', help='which algorithm?', choices=['human', 'bfs', 'astar'])
	args = parser.parse_args()
	if int(args.size) < 3:
		print "Invalid board size: %d; default board size to 3" % int(args.size)
		args.size = 3
	return int(args.size), args.define, args.fn

def run(size, define, fn):
	"""
	Run the n-puzzle game
	"""

	# Make a board
	if not define:
		b1 = board.Board(size)
	else:
		print '---------------------------------------'
		print 'Create a board of size %d' % size
		print '---------------------------------------'
		tiles = []
		while len(tiles) < size**2:
			tiles.append(int(raw_input('Enter Number: ')))
		b1 = board.Board(size, tiles)


	# Start game
	print '---------------------------------------'
	print 'Started %d-puzzle game' % (size**2 - 1)
	print '---------------------------------------'
	b1.printBoard()

	# Solve game
	if fn == 'human':
		while True:
			# Enter r/l/u/d/q for right/left/up/down/quit
			action = raw_input('Enter move (l/r/u/d/q):')
			if action == 'q':
				print 'You quit the game!'
				break
			b1 = b1.move(action)
			if b1.wins():
				print 'You Win!!!'
				break
	else:
		# get the steps with BFS or Astar
		if fn == 'bfs':
			actions = BFS(b1)
		else:
			assert(fn == 'astar')
			actions = Astar(b1)

		# Execute the actions
		for action in actions:
			b1 = b1.move(action)
		if b1.wins():
			print 'You Win with %s!!!' % fn.upper()
		else:
			print 'You %s did not solve the puzzle :(' % fn.upper()

def BFS(board):
	"""
		BFS algorithm for solving the n-puzzle game

		HINTS:
		1) Possible moves: l/r/u/d for left/right/up/down
		2) Use board.isLegal(move) to check if a move is legal
		3) Get all the legal moves of the current state.
		   Expand the next states with BFS (FIFO)

		Comment out the print and sys.exit(1) when you finished implementing

	"""
	""" ENTER YOUR CODE HERE """

	print "BFS not implemented"
	sys.exit(1)

def Astar(board):
	"""
		Astar algorithm for solving the n-puzzle game

		HINTS:
		1) Process similar to BFS
		2) Astar expands the states with a priority queue

		Comment out the print and sys.exit(1) when you finished implementing

	"""
	""" ENTER YOUR CODE HERE """

	print "ASTAR not implemented"
	sys.exit(1)

def isSolvable(board):
	"""
		What if board is not solvable?
	"""
	""" ENTER YOUR CODE HERE """
	
	print "isSolvable() not implemented"
	sys.exit(1)

if __name__ == '__main__':
	size, define, fn = parseCommand(sys.argv)
	run(size, define, fn)