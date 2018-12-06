
class Worker:
	def __init__(self):
		self.row = -1
		self.col = -1
		self.level = 0


class Player:
	def __init__(self):
		self.worker1 = Worker()
		self.worker2 = Worker()
		self.lastMovedWorker = ''
		self.previousPosition = [-1, -1]

	def moveWorker(self, workerNum, row, col):
		moveSuccessful = False
		if workerNum == 1:
			neighboringPositions = self.getNeighboringPositions(self.worker1)
			if [row, col] in neighboringPositions:
				self.worker1.row = row
				self.worker1.col = col
				self.lastMovedWorker = 'worker1'
				print('Moved to neighbor')
				moveSuccessful = True
			else:
				print('Invalid move')
		elif workerNum == 2:
			neighboringPositions = self.getNeighboringPositions(self.worker2)
			if [row, col] in neighboringPositions:
				self.worker2.row = row
				self.worker2.col = col
				self.lastMovedWorker = 'worker2'
				print('Moved to neighbor')
				moveSuccessful = True
			else:
				print('Invalid move')
		return moveSuccessful

	def getNeighboringPositions(self, workerPos):
		possiblePositions = []
		if self.validatePosition([workerPos.row - 1, workerPos.col]):
			possiblePositions.append([workerPos.row - 1, workerPos.col])
		if self.validatePosition([workerPos.row - 1, workerPos.col + 1]):
			possiblePositions.append([workerPos.row - 1, workerPos.col + 1])
		if self.validatePosition([workerPos.row - 1, workerPos.col - 1]):
			possiblePositions.append([workerPos.row - 1, workerPos.col - 1])
		if self.validatePosition([workerPos.row, workerPos.col + 1]):
			possiblePositions.append([workerPos.row, workerPos.col + 1])
		if self.validatePosition([workerPos.row, workerPos.col - 1]):
			possiblePositions.append([workerPos.row, workerPos.col - 1])
		if self.validatePosition([workerPos.row + 1, workerPos.col]):
			possiblePositions.append([workerPos.row + 1, workerPos.col])
		if self.validatePosition([workerPos.row + 1, workerPos.col + 1]):
			possiblePositions.append([workerPos.row + 1, workerPos.col + 1])
		if self.validatePosition([workerPos.row + 1, workerPos.col - 1]):
			possiblePositions.append([workerPos.row + 1, workerPos.col - 1])
		return possiblePositions

	def validatePosition(self, position):
		return position[0] >= 0 and position[1] >= 0 and position[0] <= 4 and position[1] <= 4

class Tile:
	level = 0
	occupied = False


def createBaseGameBoard():
	gameBoard = [[Tile(), Tile(), Tile(), Tile(), Tile()],
	[Tile(), Tile(), Tile(), Tile(), Tile()],
	[Tile(), Tile(), Tile(), Tile(), Tile()],
	[Tile(), Tile(), Tile(), Tile(), Tile()],
	[Tile(), Tile(), Tile(), Tile(), Tile()]]
	return gameBoard


def printGameBoard(gameBoard):
	for rowIndex in range(len(gameBoard)):
		rowStr = ''
		for colIndex in range(len(gameBoard[rowIndex])):
			if gameBoard[rowIndex][colIndex].occupied:
				rowStr += 'True   '
			else:
				rowStr += 'False  '
		print(rowStr)
	print()


def placeInitialWorker(gameBoard, Player, workerNum, row, col):
	if gameBoard[row][col].occupied == False:
		Player.moveWorker(gameBoard, workerNum, row, col)
		gameBoard[row][col].occupied = True
	else:
		print('A worker is already there!')


def moveWorker(gameBoard, Player, workerNum, row, col):
	successful = Player.moveWorker(gameBoard, workerNum)


def validateMove(gameBoard, player, workerNum, row, col)
	if workerNum = 1:
		workerLevel = player.worker1.level
		
if __name__ == '__main__':
	# Setup Game
	player1 = Player()
	player2 = Player()
	gameBoard = createBaseGameBoard()
	printGameBoard(gameBoard)
	
	# Player1 places workers
	placeInitialWorker(gameBoard, player1, 1, 2, 1)
	placeInitialWorker(gameBoard, player1, 2, 3, 1)
	printGameBoard(gameBoard)
	
	# Player2 places workers
	placeInitialWorker(gameBoard, player2, 1, 2, 4)
	placeInitialWorker(gameBoard, player2, 2, 3, 4)
	
	# Player1 makes a move
	successful = moveWorker(gameBoard, 1, 2, 2)
	printGameBoard(gameBoard)
