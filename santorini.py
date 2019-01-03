import player
import gameBoard
import random
import minimax
from numpy import inf

if __name__ == '__main__':
	# Setup Game
	player1 = player.Player(0)
	player2 = player.Player(1)
	players = [player1, player2]
	myGameBoard = gameBoard.GameBoard()
	myGameBoard.printGameBoardWorkers(-1, -1, players)
	
	# Initial worker placement
	# for playerNum in range(2):
	# 	for workerNum in range(2):
	# 		placedWorker = False
	# 		while placedWorker == False:
	# 			row = random.randint(0, 4)
	# 			col = random.randint(0, 4)
	# 			placedWorker = myGameBoard.placeInitialWorker(players[playerNum], workerNum, row, col)
	# 	myGameBoard.printGameBoardWorkers(-1, -1, players)
	myGameBoard.placeInitialWorker(players[0], 0, 0, 0)
	myGameBoard.placeInitialWorker(players[0], 1, 0, 1)
	myGameBoard.placeInitialWorker(players[1], 0, 1, 0)
	myGameBoard.placeInitialWorker(players[1], 1, 1, 1)
	for turnNum in range(100):
		print('TURN: ', turnNum)
		playerNum = turnNum % 2
		print('PLAYER NUM: ', playerNum)
		rootNode = minimax.buildTree(playerNum, players, myGameBoard)
		if len(rootNode.childNodes) == 0:
			print('No Moves Left - Player ' + str(playerNum) + ' Loses')
			break
		bestVal, bestActionSet = minimax.minimax(rootNode, 2, True, -inf, +inf)
		bestMove = bestActionSet[1]
		bestWorkerNum = bestActionSet[0]
		print('BEST VAL: ', bestVal)
		# bestMove, bestWorkerNum = minimax.oneDeepBestAction(players[playerNum], myGameBoard)
		print('-- MOVING WORKER --')
		oldPos = [players[playerNum].workers[bestWorkerNum].row, players[playerNum].workers[bestWorkerNum].col]
		print('CUR POS', oldPos)
		# Make a move
		myGameBoard.moveWorker(players[playerNum], bestWorkerNum, bestMove[0], bestMove[1])
		newPos = [bestMove[0], bestMove[1]]
		print('MOVED TO: ', newPos)
		print('-- MOVE COMPLETE --')
		if myGameBoard.checkForWinner():
			print('!! WINNER !!')
			print('PLAYER: ', playerNum)
			print('TURN: ', turnNum)
			break
		print('-- BUILDING --')
		# Make a build
		myGameBoard.buildLevel(players[playerNum], bestMove[2], bestMove[3])
		print('BUILT AT: ', [bestMove[2], bestMove[3]])
		print('-- BUILD COMPLETE --')
		myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
		myGameBoard.printGameBoardLevels()
	myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
	myGameBoard.printGameBoardLevels()
	print('DONE')
