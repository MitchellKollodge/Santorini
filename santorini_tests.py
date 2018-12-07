import unittest
import santorini
import gameBoard
import worker
import player


class GameBoardTests(unittest.TestCase):

#################################
##  getNeighboringPositions()  ##
#################################
	def test_getNeighboringPositions_TopLeftCorner(self):
		myWorker = worker.Worker()
		worker.row = 0
		worker.col = 0
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker)
		self.assertEqual([[0, 1], [1, 0], [1, 1]], neighboringPositions)

	def test_getNeighboringPositions_BottomRightCorner(self):
		myWorker = worker.Worker()
		worker.row = 4
		worker.col = 4
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker)
		self.assertEqual([[3, 4], [3, 3], [4, 3]], neighboringPositions)

	def test_getNeighboringPositions_Center(self):
		myWorker = worker.Worker()
		worker.row = 2
		worker.col = 2
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker)
		self.assertEqual([[1, 2], [1, 3], [1, 1], [2, 3], [2, 1], [3, 2], [3, 3], [3, 1]], neighboringPositions)

####################
##  moveWorker()  ##
####################
	def test_moveWorker_OnePosRightSameLevelValid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myPlayer.workers[0].level = 0
		myGameBoard.gameBoard[0][0].occupied = True
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 1)
		self.assertTrue(successful and
						myGameBoard.gameBoard[0][0].occupied == False and
						myGameBoard.gameBoard[0][1].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 1 and
						myPlayer.workers[0].level == 0 and
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.previousPositionWorker.level == 0 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightSameLevelInvalid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 4
		myPlayer.workers[0].level = 0
		myGameBoard.gameBoard[0][0].occupied = True
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 5)
		self.assertFalse(successful and
						myGameBoard.gameBoard[0][4].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 4 and
						myPlayer.workers[0].level == 0)

	def test_moveWorker_OnePosRightUpOneLevelValid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myPlayer.workers[0].level = 0
		myGameBoard.gameBoard[0][0].occupied = True
		myGameBoard.gameBoard[0][1].level = 1
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 1)
		self.assertTrue(successful and
						myGameBoard.gameBoard[0][0].occupied == False and
						myGameBoard.gameBoard[0][1].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 1 and
						myPlayer.workers[0].level == 1 and
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.previousPositionWorker.level == 0 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightUpTwoLevelsInvalid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myPlayer.workers[0].level = 0
		myGameBoard.gameBoard[0][0].occupied = True
		myGameBoard.gameBoard[0][1].level = 2
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 1)
		self.assertFalse(successful and
						myGameBoard.gameBoard[0][0].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 1 and
						myPlayer.workers[0].level == 0)

	def test_moveWorker_OnePosRightDownOneLevelValid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myPlayer.workers[0].level = 1
		myGameBoard.gameBoard[0][0].occupied = True
		myGameBoard.gameBoard[0][1].level = 0
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 1)
		self.assertTrue(successful and
						myGameBoard.gameBoard[0][0].occupied == False and
						myGameBoard.gameBoard[0][1].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 1 and
						myPlayer.workers[0].level == 0 and
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.previousPositionWorker.level == 1 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightDownTwoLevelsValid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myPlayer.workers[0].level = 2
		myGameBoard.gameBoard[0][0].occupied = True
		myGameBoard.gameBoard[0][1].level = 0
		successful = myGameBoard.moveWorker(myPlayer, 0, 0, 1)
		self.assertTrue(successful and
						myGameBoard.gameBoard[0][0].occupied == False and
						myGameBoard.gameBoard[0][1].occupied == True and
						myPlayer.workers[0].row == 0 and
						myPlayer.workers[0].col == 1 and
						myPlayer.workers[0].level == 0 and
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.previousPositionWorker.level == 2 and
						myPlayer.lastMovedWorker == 0)

############################
##  placeInitialWorker()  ##
############################
	def test_placeInitialWorker_CenterValid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, 2, 2)
		self.assertTrue(successful and myGameBoard.gameBoard[2][2].occupied)

	def test_placeInitialWorker_CenterInvalid(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[2][2].occupied = True
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, 2, 2)
		self.assertFalse(successful and myGameBoard.gameBoard[2][2].occupied)

	def test_placeInitialWorker_InvalidPos(self):
		myPlayer = player.Player()
		myGameBoard = gameBoard.GameBoard()
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, -1, 0)
		self.assertFalse(successful)

###########################
##  validateMoveLevel()  ##
###########################
	def test_validateMoveLevel_SameLevelValid(self):
		myWorker = worker.Worker()
		myWorker.level = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		self.assertTrue(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_UpOneLevelValid(self):
		myWorker = worker.Worker()
		myWorker.level = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 1
		self.assertTrue(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_UpOneLevelInvalid(self):
		myWorker = worker.Worker()
		myWorker.level = 3
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 4
		self.assertFalse(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_UpTwoLevelsInvalid(self):
		myWorker = worker.Worker()
		myWorker.level = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 2
		self.assertFalse(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_DownOneLevelValid(self):
		myWorker = worker.Worker()
		myWorker.level = 1
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		self.assertTrue(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_DownOneLevelInValid(self):
		myWorker = worker.Worker()
		myWorker.level = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = -1
		self.assertFalse(myGameBoard.validateMoveLevel(myWorker, 0, 0))

	def test_validateMoveLevel_DownTwoLevelsValid(self):
		myWorker = worker.Worker()
		myWorker.level = 2
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		self.assertTrue(myGameBoard.validateMoveLevel(myWorker, 0, 0))

##########################
##  validatePosition()  ##
##########################
	def test_validatePosition_TopLeftCornerValidPos(self):
		self.assertTrue(gameBoard.GameBoard().validatePosition(0, 0))

	def test_validatePosition_BottomRightCornerValidPos(self):
		self.assertTrue(gameBoard.GameBoard().validatePosition(4, 4))

	def test_validatePosition_LeftEdgeInvalidPos(self):
		self.assertFalse(gameBoard.GameBoard().validatePosition(2, -1))

	def test_validatePosition_RightEdgeInvalidPos(self):
		self.assertFalse(gameBoard.GameBoard().validatePosition(2, 5))

	def test_validatePosition_TopEdgeInvalidPos(self):
		self.assertFalse(gameBoard.GameBoard().validatePosition(-1, 0))

	def test_validatePosition_BottomEdgeInvalidPos(self):
		self.assertFalse(gameBoard.GameBoard().validatePosition(5, 0))

############################
##  workersWillCollide()  ##
############################
	def test_workersWillCollide_NoCollision(self):
		myGameBoard = gameBoard.GameBoard()
		self.assertFalse(myGameBoard.workersWillCollide(2, 2))

	def test_workersWillCollide_Collision(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[2][2].occupied = True
		self.assertTrue(myGameBoard.workersWillCollide(2, 2))

if __name__ == '__main__':
	unittest.main()
