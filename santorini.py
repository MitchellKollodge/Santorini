import player
import gameBoard

if __name__ == '__main__':
	# Setup Game
	player1 = player.Player()
	player2 = player.Player()
	players = [player1, player2]
	myGameBoard = gameBoard.GameBoard()
	myGameBoard.printGameBoard()
	
	# Player1 places workers
	print('PLAYER 1: INITIAL PLACEMENT')
	myGameBoard.placeInitialWorker(players[0], 0, 2, 1)
	myGameBoard.placeInitialWorker(players[0], 1, 3, 1)
	myGameBoard.printGameBoard()
	
	# Player2 places workers
	print('PLAYER 2: INITIAL PLACEMENT')
	myGameBoard.placeInitialWorker(players[1], 0, 2, 4)
	myGameBoard.placeInitialWorker(players[1], 1, 3, 4)
	myGameBoard.printGameBoard()
	
	# Player1 makes a move
	print('PLAYER 1: MOVE 1')
	successful = False
	while successful == False:
		successful = myGameBoard.moveWorker(players[0], 0, 2, 2)
	myGameBoard.printGameBoard()
	
	# Player1 builds
	print('PLAYER 1: BUILD 1')
