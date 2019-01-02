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


	def evaluateGameBoard(self, playerNum):
		heightValue = [0, 30, 90, 9000]
		value = 0
		for row in range(len(self.gameBoard)):
			for col in range(len(self.gameBoard[row])):
				if self.gameBoard[row][col].occupyingPlayer == playerNum:
					value += heightValue[self.gameBoard[row][col].level]
				elif self.gameBoard[row][col].occupied:
					value -= heightValue[self.gameBoard[row][col].level]
		return value


	def getAllMoveAndBuildCombos(self, workerNum, row, col):
		combos = []
		allValidMoves = self.getValidMoves(row, col)
		for move in allValidMoves:
			validBuilds = self.getValidBuilds(move[0], move[1])
			validBuilds.append([row, col])
			for build in validBuilds:
				combos.append([workerNum, move + build])
		return combos


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


	def getValidBuilds(self, row, col):
		validBuilds = []
		neighboringPositions = self.getNeighboringPositions(row, col)
		for pos in neighboringPositions:
			if self.verifyValidBuild(pos[0], pos[1]):
				validBuilds.append(pos)
		return validBuilds


	def getValidMoves(self, row, col):
		validMoves = []
		neighboringPositions = self.getNeighboringPositions(row, col)
		for pos in neighboringPositions:
			if self.validateMoveLevel(row, col, pos[0], pos[1]) and not self.workersWillCollide(pos[0], pos[1]):
				validMoves.append(pos)
		return validMoves


# Tests written
	def moveWorker(self, player, workerNum, row, col):
		if [row, col] in self.getNeighboringPositions(player.workers[workerNum].row, player.workers[workerNum].col):
			if self.workersWillCollide(row, col) == False and self.validateMoveLevel(player.workers[workerNum].row, player.workers[workerNum].col, row, col):
				player.previousPositionWorker.row = player.workers[workerNum].row
				player.previousPositionWorker.col = player.workers[workerNum].col
				player.workers[workerNum].row = row
				player.workers[workerNum].col = col
				player.lastMovedWorker = workerNum
				self.gameBoard[player.previousPositionWorker.row][player.previousPositionWorker.col].occupied = False
				self.gameBoard[row][col].occupied = True
				self.gameBoard[player.previousPositionWorker.row][player.previousPositionWorker.col].occupyingPlayer = None
				self.gameBoard[row][col].occupyingPlayer = player.playerNum
				return True
		return False


# Tests written
	def placeInitialWorker(self, player, workerNum, row, col):
		if self.workersWillCollide(row, col) == False and self.validatePosition(row, col):
			player.previousPositionWorker.row = row
			player.previousPositionWorker.col = col
			player.workers[workerNum].row = row
			player.workers[workerNum].col = col
			player.lastMovedWorker = workerNum
			self.gameBoard[row][col].occupied = True
			self.gameBoard[row][col].occupyingPlayer = player.playerNum
			return True
		return False


	def printGameBoardLevels(self):
		for rowIndex in range(len(self.gameBoard)):
			rowStr = ''
			for colIndex in range(len(self.gameBoard[rowIndex])):
				rowStr += str(self.gameBoard[rowIndex][colIndex].level) + '  '
			print(rowStr)
		print()


	def printGameBoardWorkers(self, oldRow, oldCol, players):
		player1Workers = players[0].workers
		player2Workers = players[1].workers
		for rowIndex in range(len(self.gameBoard)):
			rowStr = ''
			for colIndex in range(len(self.gameBoard[rowIndex])):
				if self.gameBoard[rowIndex][colIndex].occupied:
					if (player1Workers[0].row == rowIndex and player1Workers[0].col == colIndex):
						rowStr += '\033[92m' + 'True 00 ' + '\033[0m'  # Green
					elif(player1Workers[1].row == rowIndex and player1Workers[1].col == colIndex):
						rowStr += '\033[92m' + 'True 01 ' + '\033[0m'  # Green
					elif(player2Workers[0].row == rowIndex and player2Workers[0].col == colIndex):
						rowStr += '\033[92m' + 'True 10 ' + '\033[0m' # Green
					else:
						rowStr += '\033[92m' + 'True 11 ' + '\033[0m'  # Green
				elif rowIndex == oldRow and colIndex == oldCol:
					if players[0].previousPositionWorker.row == oldRow and players[0].previousPositionWorker.col == oldCol:
						rowStr += '\033[33m' + 'False0  ' + '\033[0m'  # Yellow
					else:
						rowStr += '\033[33m' + 'False1  ' + '\033[0m'  # Yellow
				else:
					rowStr += 'False   '
			print(rowStr)
		print()


# Tests written
	def validateMoveLevel(self, oldRow, oldCol, newRow, newCol):
		currentWorkerLevel = self.gameBoard[oldRow][oldCol].level
		moveLevel = self.gameBoard[newRow][newCol].level
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
