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
		oldPos = [-1, -1]
		newPos = [-1, -1]
		playerNum = turnNum % 2
		movedWorker = False
		print('MOVING')
		workerNum = random.randint(0, 1)
		validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum])
		if len(validMoves) == 0 and workerNum == 0:
			workerNum = 1
			validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum])
		elif len(validMoves) == 0 and workerNum == 1:
			workerNum = 0
			validMoves = myGameBoard.getValidMoves(players[playerNum].workers[workerNum])
		if len(validMoves) == 0:
			print('No moves left')
			t = input('hi')
		print('CUR POS', players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col)
		while movedWorker == False:
			print('VALID MOVES: ', validMoves)
			if len(validMoves) == 0:
				name = input('hi')
			choiceMove = random.randint(0, len(validMoves) - 1)
			oldPos = [players[playerNum].workers[workerNum].row, players[playerNum].workers[workerNum].col]
			movedWorker = myGameBoard.moveWorker(players[playerNum], workerNum, validMoves[choiceMove][0], validMoves[choiceMove][1])
			if movedWorker:
				newPos = [validMoves[choiceMove][0], validMoves[choiceMove][1]]
				print('Moved to: ', validMoves[choiceMove][0], validMoves[choiceMove][1])
		print('MOVE COMPLETE')
		if myGameBoard.checkForWinner():
			print('WINNER')
			print('PLAYER: ', playerNum)
			print('TURN: ', turnNum)
			break
		buildComplete = False
		print('BUILDING')
		while buildComplete == False:
			row = random.randint(0, 4)
			col = random.randint(0, 4)
			buildComplete = myGameBoard.buildLevel(players[playerNum], row, col)
		print('BUILD COMPLETE')
		print('EVAL: ', myGameBoard.evaluateGameBoard(players[playerNum], players))
		myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
		myGameBoard.printGameBoardLevels()
	myGameBoard.printGameBoardWorkers(oldPos[0], oldPos[1], players)
	myGameBoard.printGameBoardLevels()
	print('DONE')
