import player
import gameBoard
import random

if __name__ == '__main__':
	# Attempt at AI
	# Setup Game
	player1 = player.Player()
	player2 = player.Player()
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
		movedWorker = False
		print('-- MOVING WORKER --')
		workerNum = random.randint(0, 1)
		validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		if len(validMoves) == 0 and workerNum == 0:
			workerNum = 1
			validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		elif len(validMoves) == 0 and workerNum == 1:
			workerNum = 0
			validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		if len(validMoves) == 0:
			print('No moves left')
			t = input('hi')
		print('CUR POS', [players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col])
		print('VALID MOVES: ', validMoves)
		print('NUM OF COMBOS: ', len(myGameBoard.getAllMoveAndBuildCombos(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)))
		print('ALL COMBOS: ', myGameBoard.getAllMoveAndBuildCombos(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col))
		if len(validMoves) == 0:
			name = input('hi')
		# Make a move
		choiceMove = random.randint(0, len(validMoves) - 1)
		oldPos = [players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col]
		myGameBoard.moveWorker(players[playerNum], workerNum, validMoves[choiceMove][0], validMoves[choiceMove][1])
		newPos = [validMoves[choiceMove][0], validMoves[choiceMove][1]]
		print('MOVED TO: ', [validMoves[choiceMove][0], validMoves[choiceMove][1]])
		print('-- MOVE COMPLETE --')
		if myGameBoard.checkForWinner():
			print('!! WINNER !!')
			print('PLAYER: ', playerNum)
			print('TURN: ', turnNum)
			break
		buildComplete = False
		print('-- BUILDING --')
		validBuilds = myGameBoard.getValidBuilds(players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		print('VALID BUILDS: ', validBuilds)
		# Make a build
		choiceBuild = random.randint(0, len(validBuilds) - 1)
		myGameBoard.buildLevel(players[playerNum], validBuilds[choiceBuild][0], validBuilds[choiceBuild][1])
		print('BUILT AT: ', [validBuilds[choiceBuild][0], validBuilds[choiceBuild][1]])
		print('-- BUILD COMPLETE --')
		print('EVAL: ', myGameBoard.evaluateGameBoard(players[playerNum], players))
		myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
		myGameBoard.printGameBoardLevels()
	myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
	myGameBoard.printGameBoardLevels()
	print('DONE')
