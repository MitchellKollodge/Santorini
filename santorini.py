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
	myGameBoard.placeInitialWorker(players[0], 1, 2, 1)
	myGameBoard.placeInitialWorker(players[0], 2, 3, 1)
	myGameBoard.printGameBoard()
	
	# Player2 places workers
	myGameBoard.placeInitialWorker(players[1], 1, 2, 4)
	myGameBoard.placeInitialWorker(players[1], 2, 3, 4)
	
	# Player1 makes a move
	successful = myGameBoard.moveWorker(players[0], 1, 2, 2)
	myGameBoard.printGameBoard()
