
class board():
	"""
		board
	"""
	def __init__(self, numPlayers=2):
		self.numPlayers = numPlayers
		self.tracks = 52
		self.homeZone = 6


	def printBoard():
		print "------------------"