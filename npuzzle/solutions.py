import sys
import board
import heapq
import random

"""
NOTE: PriorityQueue Class taken from Berkley's CS 188 pacman project
"""
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

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

	# b1 = board.Board(3,[0,1,2,3,4,5,6,7,8])
	# b1 = b1.move('d')
	# b1 = b1.move('d')
	# b1 = b1.move('r')
	# b1 = b1.move('r')
	# b1 = b1.move('u')
	# b1 = b1.move('u')
	# b1 = b1.move('l')
	# b1 = b1.move('l')
	# b1 = b1.move('d')
	# b1 = b1.move('r')
	# b1 = b1.move('r')

	# b1 = board.Board(3,[1,2,4,5,0,3,6,7,8])
	# b1 = board.Board(4,[9,4,6,5,8,0,11,1,13,7,3,2,12,14,10,15])	
	b1 = board.Board(4,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
	acts = ['l','r','u','d']
	for i in range(70):
		legs = []
		for act in acts:
			if b1.isLegal(act):
				legs.append(act)
		m = legs[random.randint(0,len(legs)-1)]
		b1 = b1.move(m)


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
			b1.printBoard()
			if b1.wins():
				print 'You Win!!!'
				break
	else:
		print 'board solvable? ', isSolvable(b1)
		# get the steps with BFS or Astar
		if fn == 'bfs':
			actions = BFS(b1)
		else:
			assert(fn == 'astar')
			actions = Astar(b1)

		# Execute the actions
		for action in actions:
			b1 = b1.move(action)
			print '---------------------------------------'
			print 'moved', action
			b1.printBoard()
		if b1.wins():
			print 'You Win with %s!!!' % fn.upper()
		else:
			print 'Your %s did not solve the puzzle :(' % fn.upper()

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

	# print "BFS not implemented"
	# sys.exit(1)


	actions = ['l','r','u','d']
	fringe = [(board,[])]
	visited = []
	count = 0
	while len(fringe) != 0:
		current_board, sol = fringe.pop(0)
		if current_board.wins():
			print "Found a solution (%d nodes expanded)" % count
			print sol
			return sol

		if current_board in visited:
			continue
		count += 1
		visited.append(current_board)
		for act in actions:
			if current_board.isLegal(act):
				new_sol = list(sol)
				new_sol.append(act)
				fringe.append((current_board.move(act), new_sol))
	print "solution not found (%d nodes expanded)" % count
	return []

def heuristic(board):
	heur = 0
	size = board.getSize()
	grid = board.getBoardAsGrid()
	for i in range(size):
		for j in range(size):
			num = board.getNum(i,j)
			heur += abs( num/size - i) + abs( num%size - j)
	return heur

def Astar(board):
	"""
		Astar algorithm for solving the n-puzzle game

		HINTS:
		1) Process similar to BFS
		2) Astar expands the states with a priority queue

		Comment out the print and sys.exit(1) when you finished implementing

	"""
	""" ENTER YOUR CODE HERE """

	actions = ['l','r','u','d']
	fringe = PriorityQueue()
	fringe.push((board,[]), 0)
	visited = []
	count = 0
	while not fringe.isEmpty():
		current_board, sol = fringe.pop()
		if current_board.wins():
			print "Found a solution (%d nodes expanded)" % count
			print sol
			return sol

		if current_board in visited:
			continue
		count += 1
		visited.append(current_board)
		for act in actions:
			if current_board.isLegal(act):
				new_sol = list(sol)
				new_sol.append(act)
				cost = len(new_sol)
				heur = heuristic(current_board)
				fringe.push((current_board.move(act), new_sol), cost + heur)
	print "solution not found"
	return []

	# print "ASTAR not implemented"
	# sys.exit(1)


def isSolvable(board):
	"""
		What if board is not solvable?
	"""
	""" ENTER YOUR CODE HERE """

	return countInv1(board.getBoardAsList()) % 2 == 0

def countInv1(list1):
	count = 0
	for i in range(0, len(list1)-1):
		for j in range(i+1, len(list1)):
			if list1[i] > list1[j]:
				count += 1
	return count

def merge_sort(list1):
	# already sorted
	size = len(list1)
	if size <= 1:
		return list(list1)
	# divide the array, sort and merge
	list2 = merge_sort(list1[0:size/2])
	list3 = merge_sort(list1[size/2:])

	return merge(list2, list3)

def merge(list1, list2):
	result = []
	inv_count = 0
	while len(list1) != 0 and len(list2) != 0:
		if list1[0] < list2[0]:
			result.append(list1[0])
			list1.pop(0)
		else:
			result.append(list2[0])
			list2.pop(0)
	for i in list1:
		result.append(i)
	for i in list2:
		result.append(i)
	return result

if __name__ == '__main__':
	size, define, fn = parseCommand(sys.argv)
	run(size, define, fn)
