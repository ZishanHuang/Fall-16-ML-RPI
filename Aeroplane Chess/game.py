import board
import random

"""
Game setup
-------------
board: 52 pieces of track on main course (4 colors) ** shortcut at specific places
	   6 pieces of track on home zone * 4 colors

player:
		1 id
		1 color
		4 pieces of chess --> hangar
						  --> landed
						  --> in air
		items


dice: basic dice --> euqal opportunity for 1-6

items:
	   cheat dice  --> 50% of executing player's defined function,
	   				   20% of rolling the basic dice,
	   				   15% of rolling the basic dice but advance twice the result: e.g. rolled 2 and advance 4 steps; maximum still 6
	  				   15% of being caught cheating and pause for one round
	   double-roll --> rolling the dice a second time
	   thunder     --> forbid one player to play for one round
	   shield	   --> protect the player from thunder for one round

rules: 1) 
"""
"""
Track settiings:
0 - not used
1 - 6: home for P1, 7,8,9: hangar, taking off, landed
10 - not used
11 - 16: home for P2, 17, 18, 19: hangar, taking off, landed
20 - not used
21 - 26: home for P3, 27, 28, 29: hangar, taking off, landed
30 - not used
31 - 36: home for P4, 37, 38, 39: hangar, taking off, landed

Medium board:
40 - 75: main course

Large board:
40 - 91: main course
"""

"""
Notes:
Players can do:
1) choose which chess to play
2) choose which player to pause
3) choose to use shield or not
4) choose to cheat (provide a cheating roll number)

Player needs to know:
1) All players' chess locations
2) All players' items
3) Uncollected items on the board

Players rolls the dice when:
1) It's the player's round
2) Player got a 6 in the last roll
3) Player can only roll for 3 consecutive terms
"""

class Game():
	"""Game"""
	def __init__(self, arg):
		self.arg = arg

	def run():
		print "run the game"
		"""
		# wait for players to connect
		while room not full
			add player when someone gets connected
			if someone is ready
				mark ready
			if all players are ready or the first person waited for 2 minutes
				break

		# start game
		while no one wins the game
			determine which player's round it is
			send message (board info) to player
			player uses an item
				receive item name
				changes state of the other player (receive playerID)
					send message to the player being attacked annd ask if use shield
					if player does not use shield (receive no or timeout)
						mute the player for one round
					send message to both informing of the result
				
				alters the dice rolling (receive the result of rolling the player's own dice)
			player roll a dice
			send dice result back
			player moves a chess (receive chessID from player)
				player might use the shortcut
				player might gain an item or sends another player's chess back
			if player wins, exit the game

		send message to everyone
		"""

	def initialize():
		print "initialize the game"

	def moveChess(playerID, chessID):
		# check if move is legal
		print "move a chess of player"

class Player():
	"""Player"""
	def __init__(self, playerName, playerID, colorAssigned, boardSize):
		self.name = playerName
		self.id = playerID
		self.color = colorAssigned
		self.boardSize = boardSize
		self.chess = [-1, -1, -1, -1]
		self.items = {'thunder':0, 'shield':0, 'cheat_dice':0}
		self.isReady = False
		self.isMuted = False

	def rollDice(self):
		return random.randint(1,6)

	def rollCheatDice(self, cheatValue):
		roll = random.ramdom()
		if roll < 0.5:
			return cheatValue
		elif roll < 0.7:
			return self.rollDice()
		elif roll < 0.85:
			return min(self.rollDice()*2, 6)
		else:
			self.Mute()
			return cheatValue
			# return 0

	def Move(self, chessID, dice):
		# chess in hangar
		if dice == 6 and self.chess[chessID] == -1:
			self.chess[chessID] = 0
		# chess ready to take off
		if self.chess[chessID] == 0:
			# track differs by boardSize and player color
			if self.boardSize == "Small":
				self.chess[chessID] += dice
			elif self.boardSize == "Medium":
				self.chess[chessID] += dice
			elif self.boardSize == "Large":
				self.chess[chessID] += dice


	# def makeMove(self):

	def getName(self):
		return self.name

	def getID(self):
		return self.id

	def getColor(self):
		return self.color

	def getChessList(self):
		return self.chess.deepcopy()

	def getChessPosition(self, index):
		return self.chess[index]

	def getItemsList(self):
		return self.items.deepcopy()

	def getNumThunders(self):
		return self.items['thunder']

	def getNumShields(self):
		return self.items['shield']

	def getNumCheatDice(self):
		return self.items['cheat_dice']

	def Wins(self):
		return self.chess.count(7) == 4

	def isReady(self):
		self.isReady = True

	def Mute(self):
		self.isMuted = True

	def UnMute(self):
		self.isMuted = False