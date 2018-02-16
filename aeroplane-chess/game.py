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
Track settings:
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

Track settings version 2:
0 - not used
1 - 6: home for all players, 7,8,9: hangar, taking off, landed
10 - 45: main course
Every player runs 34 tracks
P1: 10 - 43
P2: 19 - 45, 10 - 16
P3: 28 - 45, 10 - 25
P4: 37 - 45, 10 - 34


P1: 11,15,19,23,27,31,35,39,43
P2: 20,24,28,32,36,40,44,12,16
P3: 29,33,37,41,45,13,17,21,25
P4: 38,42,10,14,18,22,26,30,34

10 - 61: main course

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
	def __init__(self):
		# self.numPlayers = numPlayers
		self.numPlayers = 0
		self.maxNumPlayers = 4
		self.minNumPlayers = 2
		self.players = []
		# self.players = [Player('ann',0,'red','Small'), Player('bob',1,'blue','Small')]

	def run(self):
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
		while self.numPlayers < self.maxNumPlayers:
			name = raw_input('Enter player name: ')
			# run small board for now
			player = Player(name,self.numPlayers,'Small')
			self.players.append(player)
			self.numPlayers += 1

		current_player = 0
		while True:
			print "Player %d's turn" % current_player
			if self.players[current_player].isMuted():
				self.players[current_player].UnMute()
				current_player = (current_player + 1) % len(self.players)
				continue
			print "Player %d's chess list:" % current_player, self.players[current_player].getChessList()
			print "Player %d's items list:" % current_player, self.players[current_player].getItemsList()

			item = raw_input('Use item?')
			# if self.players[current_player].getItemsList()

			dice = self.players[current_player].rollDice()
			print "Player %d rolled %d" %(current_player, dice)
			cid = int(raw_input("Which chess to move?"))
			self.players[current_player].Move(cid, dice)
			print "Player %d's chess list:" % current_player, self.players[current_player].getChessList()
			if self.players[current_player].Wins():
				print "Player %d wins!!!" % current_player
				break
			if dice != 6:
				current_player = (current_player + 1) % len(self.players)

class Player():
	"""Player"""
	def __init__(self, playerName, playerID, boardSize):
		self.name = playerName
		self.id = playerID
		self.boardSize = boardSize
		self.chess = [-1, -1, -1, -1]
		self.items = {'thunder':0, 'shield':0, 'cheat_dice':0}
		# self.isReady = False
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
		print "move chess %d forward by %d" %(chessID, dice)
		# chess in hangar
		if self.chess[chessID] == -1:
			if dice == 6:
				self.chess[chessID] = 0
				# print 'i should exit here'
			# return
		# chess ready to take off
		elif self.chess[chessID] == 0:
			if self.boardSize == "Small":
				self.chess[chessID] += dice
			else:
				# for medium and large board, main course starts at 8
				self.chess[chessID] += 7 + dice

		elif self.chess[chessID] < 7:
			# ru;es at home zone same for all board sizes
			if self.chess[chessID] + dice <= 7:
				self.chess[chessID] += dice
			else:
				self.chess[chessID] = 14 - (self.chess[chessID] + dice)
		elif self.chess[chessID] == 7:
			return
		else:
			# this section should not be entered when board size is small
			assert(self.boardSize != "Small")
			'''
			if self.boardSize == "Small":
				self.chess[chessID] += dice
			elif self.boardSize == "Medium":
				self.chess[chessID] += dice
			elif self.boardSize == "Large":
				self.chess[chessID] += dice
			'''
			
		print "chess %d position: %d" %(chessID, self.chess[chessID])


	def canJump(self, chessID, position):
		# depend on track...
		if position % self.playerID == 0:
			return True
		return False

	def Jump(self, chessID):
		self.chess[chessID] += 4

	# def makeMove(self):

	def getName(self):
		return self.name

	def getID(self):
		return self.id

	def getChessList(self):
		return list(self.chess)

	def getChessPosition(self, index):
		return self.chess[index]

	def getItemsList(self):
		return list(self.items)

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