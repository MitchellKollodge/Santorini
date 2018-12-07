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


	def getNeighboringPositions(self, workerPos):
		possiblePositions = []
		if self.validatePosition(workerPos.row - 1, workerPos.col):
			possiblePositions.append([workerPos.row - 1, workerPos.col])
		if self.validatePosition(workerPos.row - 1, workerPos.col + 1):
			possiblePositions.append([workerPos.row - 1, workerPos.col + 1])
		if self.validatePosition(workerPos.row - 1, workerPos.col - 1):
			possiblePositions.append([workerPos.row - 1, workerPos.col - 1])
		if self.validatePosition(workerPos.row, workerPos.col + 1):
			possiblePositions.append([workerPos.row, workerPos.col + 1])
		if self.validatePosition(workerPos.row, workerPos.col - 1):
			possiblePositions.append([workerPos.row, workerPos.col - 1])
		if self.validatePosition(workerPos.row + 1, workerPos.col):
			possiblePositions.append([workerPos.row + 1, workerPos.col])
		if self.validatePosition(workerPos.row + 1, workerPos.col + 1):
			possiblePositions.append([workerPos.row + 1, workerPos.col + 1])
		if self.validatePosition(workerPos.row + 1, workerPos.col - 1):
			possiblePositions.append([workerPos.row + 1, workerPos.col - 1])
		return possiblePositions


	# Needs testing
	def moveWorker(self, player, workerNum, row, col):
		if self.workersWillCollide(row, col) == False and self.validateMoveLevel(player.workers[workerNum], row, col):
			if [row, col] in self.getNeighboringPositions(player.workers[workerNum]):
				player.previousPositionWorker.row = player.workers[workerNum].row
				player.previousPositionWorker.col = player.workers[workerNum].col
				player.previousPositionWorker.level = player.workers[workerNum].level
				player.workers[workerNum].row = row
				player.workers[workerNum].col = col
				player.workers[workerNum].level = self.gameBoard[row][col].level
				player.lastMovedWorker = workerNum
				self.gameBoard[player.previousPositionWorker.row][player.previousPositionWorker.col].occupied = False
				self.gameBoard[row][col].occupied = True
				return True
		return False


	# Needs testing
	def placeInitialWorker(self, player, workerNum, row, col):
		if self.workersWillCollide(row, col) == False and self.validatePosition(row, col):
			player.previousPositionWorker.row = row
			player.previousPositionWorker.col = col
			player.previousPositionWorker.level = self.gameBoard[row][col].level
			player.workers[workerNum].row = row
			player.workers[workerNum].col = col
			player.workers[workerNum].level = self.gameBoard[row][col].level
			player.lastMovedWorker = workerNum
			self.gameBoard[row][col].occupied = True
			return True
		return False


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


	# Needs testing
	def validateMoveLevel(self, worker, row, col):
		currentWorkerLevel = worker.level
		moveLevel = self.gameBoard[row][col].level
		if moveLevel == 4 or moveLevel - currentWorkerLevel > 1:
			return False
		return True


	# Needs testing
	def validatePosition(self, row, col):
		return row >= 0 and col >= 0 and row <= 4 and col <= 4


	# Needs testing
	def workersWillCollide(self, row, col):
		return self.gameBoard[row][col].occupied