import player
import gameBoard
import random
import minimax

if __name__ == '__main__':
	# Attempt at AI
	# Setup Game
	player1 = player.Player(0)
	player2 = player.Player(1)
	players = [player1, player2]
	myGameBoard = gameBoard.GameBoard()
	myGameBoard.printGameBoardWorkers(-1, -1, players)
	
	# Initial worker placement
	for playerNum in range(2):
		for workerNum in range(2):
			placedWorker = False
			while placedWorker == False:
				row = random.randint(0, 4)
				col = random.randint(0, 4)
				placedWorker = myGameBoard.placeInitialWorker(players[playerNum], workerNum, row, col)
		myGameBoard.printGameBoardWorkers(-1, -1, players)
	
	for turnNum in range(100):
		print('TURN: ', turnNum)
		oldPos = [-1, -1]
		newPos = [-1, -1]
		playerNum = turnNum % 2
		print('PLAYER NUM: ', playerNum)
		bestMove, bestWorkerNum = minimax.createTree(players[playerNum], myGameBoard)
		movedWorker = False
		print('-- MOVING WORKER --')
		workerNum = random.randint(0, 1)
		validMovesWorker1 = myGameBoard.getValidMoves(players[playerNum].workers[0].row, players[playerNum].workers[0].col)
		validMovesWorker2 = myGameBoard.getValidMoves(players[playerNum].workers[1].row, players[playerNum].workers[1].col)
		validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		if len(validMoves) == 0:
			print('No moves left')
			t = input('hi')
		oldPos = [players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col]
		print('CUR POS', oldPos)
		print('VALID MOVES: ', validMovesWorker1 + validMovesWorker2)
		# Make a move
		myGameBoard.moveWorker(players[playerNum], workerNum, bestMove[0], bestMove[1])
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
		print('EVAL: ', myGameBoard.evaluateGameBoard(playerNum))
		myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
		myGameBoard.printGameBoardLevels()
	myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
	myGameBoard.printGameBoardLevels()
	print('DONE')
