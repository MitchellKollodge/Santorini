import worker
import gameBoard

class Player:
	def __init__(self):
		self.worker1 = worker.Worker()
		self.worker2 = worker.Worker()
		self.workers = [self.worker1, self.worker2]
		self.lastMovedWorker = -1
		self.previousPositionWorker = worker.Worker()