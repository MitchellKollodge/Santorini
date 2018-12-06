import worker

class Player:
	def __init__(self):
		self.worker1 = worker.Worker()
		self.worker2 = worker.Worker()
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

	def placeInitialWorker(self, gameBoard, workerNum, row, col):
		if workerNum == 1 and self.validatePosition([row, col]):
			self.worker1.row = row
			self.worker1.col = col
		elif workerNum == 2 and self.validatePosition([row, col]):
			self.worker2.row = row
			self.worker2.col = col
