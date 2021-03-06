import unittest
import santorini
import gameBoard
import worker
import player


class GameBoardTests(unittest.TestCase):

##################
## buildLevel() ##
##################
	def test_buildLevel_EmptyTile(self):
		myGameBoard = gameBoard.GameBoard()
		myPlayer = player.Player(0)
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myGameBoard.gameBoard[0][0].occupied = True
		self.assertTrue(myGameBoard.buildLevel(myPlayer, 0, 1))

	def test_buildLevel_UnderWorker(self):
		myGameBoard = gameBoard.GameBoard()
		myPlayer = player.Player(0)
		myPlayer.workers[0].row = 0
		myPlayer.workers[0].col = 0
		myGameBoard.gameBoard[0][0].occupied = True
		self.assertFalse(myGameBoard.buildLevel(myPlayer, 0, 0))

#################################
##  getNeighboringPositions()  ##
#################################
	def test_getNeighboringPositions_TopLeftCorner(self):
		myWorker = worker.Worker()
		worker.row = 0
		worker.col = 0
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker.row, worker.col)
		self.assertEqual([[0, 1], [1, 0], [1, 1]], neighboringPositions)

	def test_getNeighboringPositions_BottomRightCorner(self):
		myWorker = worker.Worker()
		worker.row = 4
		worker.col = 4
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker.row, worker.col)
		self.assertEqual([[3, 4], [3, 3], [4, 3]], neighboringPositions)

	def test_getNeighboringPositions_Center(self):
		myWorker = worker.Worker()
		worker.row = 2
		worker.col = 2
		neighboringPositions = gameBoard.GameBoard().getNeighboringPositions(worker.row, worker.col)
		self.assertEqual([[1, 2], [1, 3], [1, 1], [2, 3], [2, 1], [3, 2], [3, 3], [3, 1]], neighboringPositions)

#####################
## getValidMoves() ##
#####################
	def test_getValidMoves_TopLeftCornerEmptyBoard(self):
		row = 0
		col = 0
		validMoves = gameBoard.GameBoard().getValidMoves(row, col)
		self.assertEqual([[0, 1], [1, 0], [1, 1]], validMoves)

	def test_getValidMoves_TopLeftCornerWithBuilds(self):
		row = 0
		col = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][1].level = 2
		validMoves = myGameBoard.getValidMoves(row, col)
		self.assertEqual([[1, 0], [1, 1]], validMoves)

	def test_getValidMoves_TopLeftCornerWithOpponent(self):
		row = 0
		col = 0
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][1].occupied = True
		validMoves = myGameBoard.getValidMoves(row, col)
		self.assertEqual([[1, 0], [1, 1]], validMoves)

##  moveWorker()  ##
####################
	def test_moveWorker_OnePosRightSameLevelValid(self):
		myPlayer = player.Player(0)
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
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightSameLevelInvalid(self):
		myPlayer = player.Player(0)
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
		myPlayer = player.Player(0)
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
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightUpTwoLevelsInvalid(self):
		myPlayer = player.Player(0)
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
		myPlayer = player.Player(0)
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
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.lastMovedWorker == 0)

	def test_moveWorker_OnePosRightDownTwoLevelsValid(self):
		myPlayer = player.Player(0)
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
						myPlayer.previousPositionWorker.row == 0 and
						myPlayer.previousPositionWorker.col == 0 and
						myPlayer.lastMovedWorker == 0)

############################
##  placeInitialWorker()  ##
############################
	def test_placeInitialWorker_CenterValid(self):
		myPlayer = player.Player(0)
		myGameBoard = gameBoard.GameBoard()
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, 2, 2)
		self.assertTrue(successful and myGameBoard.gameBoard[2][2].occupied)

	def test_placeInitialWorker_CenterInvalid(self):
		myPlayer = player.Player(0)
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[2][2].occupied = True
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, 2, 2)
		self.assertFalse(successful and myGameBoard.gameBoard[2][2].occupied)

	def test_placeInitialWorker_InvalidPos(self):
		myPlayer = player.Player(0)
		myGameBoard = gameBoard.GameBoard()
		successful = myGameBoard.placeInitialWorker(myPlayer, 0, -1, 0)
		self.assertFalse(successful)

###########################
##  validateMoveLevel()  ##
###########################
	def test_validateMoveLevel_SameLevelValid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		self.assertTrue(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_UpOneLevelValid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 1
		self.assertTrue(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_UpOneLevelInvalid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 4
		myGameBoard.gameBoard[1][0].level = 3
		self.assertFalse(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_UpTwoLevelsInvalid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 2
		myGameBoard.gameBoard[1][0].level = 0
		self.assertFalse(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_DownOneLevelValid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		myGameBoard.gameBoard[1][0].level = 1
		self.assertTrue(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_DownOneLevelInvalid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = -1
		self.assertFalse(myGameBoard.validateMoveLevel(1, 0, 0, 0))

	def test_validateMoveLevel_DownTwoLevelsValid(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 0
		myGameBoard.gameBoard[1][0].level = 2
		self.assertTrue(myGameBoard.validateMoveLevel(1, 0, 0, 0))

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

########################
## verifyValidBuild() ##
########################
	def test_verifyValidBuild_emptyTile(self):
		myGameBoard = gameBoard.GameBoard()
		self.assertTrue(myGameBoard.verifyValidBuild(0, 0))

	def test_verifyValidBuild_tileWithWorker(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].occupied = True
		self.assertFalse(myGameBoard.verifyValidBuild(0, 0))

	def test_verifyValidBuild_tileMaxLevel(self):
		myGameBoard = gameBoard.GameBoard()
		myGameBoard.gameBoard[0][0].level = 4
		self.assertFalse(myGameBoard.verifyValidBuild(0, 0))

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
