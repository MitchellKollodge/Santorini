import tile


class GameBoard:
	def __init__(self):
		self.gameBoard = self.createBaseGameBoard()


	def createBaseGameBoard(self):
		gameBoard = [[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()]]
		return gameBoard


	def printGameBoard(self):
		for rowIndex in range(len(self.gameBoard)):
			rowStr = ''
			for colIndex in range(len(self.gameBoard[rowIndex])):
				if self.gameBoard[rowIndex][colIndex].occupied:
					rowStr += 'True   '
				else:
					rowStr += 'False  '
			print(rowStr)
		print()


	def placeInitialWorker(self, Player, workerNum, row, col):
		if self.gameBoard[row][col].occupied == False:
			Player.placeInitialWorker(self.gameBoard, workerNum, row, col)
			self.gameBoard[row][col].occupied = True
			return True
		else:
			return False


	def moveWorker(self, Player, workerNum, row, col):
		if self.workersWillCollide == False and self.validateMoveLevel:
			successful = Player.moveWorker(workerNum, row, col)


	def workersWillCollide(self, row, col):
		return self.gameBoard[row][col].occupied


	def validateMoveLevel(self, worker, row, col):
		currentWorkerLevel = worker.level
		moveLevel = self.gameBoard[row][col].level
		if moveLevel == 4 or moveLevel - currentWorkerLevel > 1:
			return False
		return True