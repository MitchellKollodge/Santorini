import tile


class GameBoard:
	def __init__(self):
		self.gameBoard = self.createBaseGameBoard()


# Tests written
	def buildLevel(self, player, row, col):
		if ([row, col] in self.getNeighboringPositions(player.workers[0].row, player.workers[0].col) or 
			[row, col] in self.getNeighboringPositions(player.workers[1].row, player.workers[1].col)):
			if self.verifyValidBuild(row, col):
				self.gameBoard[row][col].level += 1
				return True
		return False


	def getValidMoves(self, worker):
		validMoves = []
		neighboringPositions = self.getNeighboringPositions(worker.row, worker.col)
		for pos in neighboringPositions:
			if self.validateMoveLevel(worker, pos[0], pos[1]) and not self.workersWillCollide(pos[0], pos[1]):
				validMoves.append(pos)
		return validMoves


	def checkForWinner(self):
		for row in range(len(self.gameBoard)):
			for col in range(len(self.gameBoard[row])):
				if self.gameBoard[row][col].level == 3 and self.gameBoard[row][col].occupied == True:
					return True
		return False


	def createBaseGameBoard(self):
		gameBoard = [[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
		[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()]]
		return gameBoard


	def evaluateGameBoard(self, currentPlayer, allPlayers):
		heightValue = [10, 30, 90, 900]
		value = 0
		for player in allPlayers:
			for worker in player.workers:
				if player == currentPlayer:
					value += heightValue[self.gameBoard[worker.row][worker.col].level]
				else:
					value -= heightValue[self.gameBoard[worker.row][worker.col].level]
		return value

# Tests written
	def getNeighboringPositions(self, row, col):
		possiblePositions = []
		if self.validatePosition(row - 1, col):
			possiblePositions.append([row - 1, col])
		if self.validatePosition(row - 1, col + 1):
			possiblePositions.append([row - 1, col + 1])
		if self.validatePosition(row - 1, col - 1):
			possiblePositions.append([row - 1, col - 1])
		if self.validatePosition(row, col + 1):
			possiblePositions.append([row, col + 1])
		if self.validatePosition(row, col - 1):
			possiblePositions.append([row, col - 1])
		if self.validatePosition(row + 1, col):
			possiblePositions.append([row + 1, col])
		if self.validatePosition(row + 1, col + 1):
			possiblePositions.append([row + 1, col + 1])
		if self.validatePosition(row + 1, col - 1):
			possiblePositions.append([row + 1, col - 1])
		return possiblePositions


# Tests written
	def moveWorker(self, player, workerNum, row, col):
		if [row, col] in self.getNeighboringPositions(player.workers[workerNum].row, player.workers[workerNum].col):
			if self.workersWillCollide(row, col) == False and self.validateMoveLevel(player.workers[workerNum], row, col):
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


# Tests written
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


	def printGameBoardLevels(self):
		for rowIndex in range(len(self.gameBoard)):
			rowStr = ''
			for colIndex in range(len(self.gameBoard[rowIndex])):
				rowStr += str(self.gameBoard[rowIndex][colIndex].level) + '  '
			print(rowStr)
		print()


	def printGameBoardWorkers(self):
		for rowIndex in range(len(self.gameBoard)):
			rowStr = ''
			for colIndex in range(len(self.gameBoard[rowIndex])):
				if self.gameBoard[rowIndex][colIndex].occupied:
					rowStr += 'True   '
				else:
					rowStr += 'False  '
			print(rowStr)
		print()


# Tests written
	def validateMoveLevel(self, worker, row, col):
		currentWorkerLevel = worker.level
		moveLevel = self.gameBoard[row][col].level
		return moveLevel < 4 and moveLevel >= 0 and moveLevel - currentWorkerLevel <= 1


# Tests written
	def validatePosition(self, row, col):
		return row >= 0 and col >= 0 and row <= 4 and col <= 4


# Tests written
	def verifyValidBuild(self, row, col):
		return self.gameBoard[row][col].level < 4 and not self.gameBoard[row][col].occupied


# Tests written
	def workersWillCollide(self, row, col):
		return self.gameBoard[row][col].occupied
