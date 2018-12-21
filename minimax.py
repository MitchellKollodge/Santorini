import copy
import gameBoard


def minimaxABP(node, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0:
        return True
    return False


def createTree(player, currentGameBoard):
    worker1row = player.workers[0].row
    worker1col = player.workers[0].col
    worker2row = player.workers[1].row
    worker2col = player.workers[1].col
    customGameBoard = gameBoard.GameBoard()
    for row in range(len(currentGameBoard.gameBoard)):
        for col in range(len(currentGameBoard.gameBoard[row])):
            customGameBoard.gameBoard[row][col] = copy.deepcopy(currentGameBoard.gameBoard[row][col])
    depth1Worker1 = customGameBoard.getAllMoveAndBuildCombos(worker1row, worker1col)
    depth1Worker2 = customGameBoard.getAllMoveAndBuildCombos(worker2row, worker2col)
    # print('LEN OF DEPTH 1: ', len(depth1Worker1) + len(depth1Worker2))
    # print('DEPTH 1: ', depth1Worker1 + depth1Worker2)

    customPlayer = copy.deepcopy(player)
    bestMove = []
    bestWorker = None
    maxScore = -9999
    for action in depth1Worker1:
        customGameBoard.gameBoard[worker1row][worker1col].occupied = False
        customGameBoard.gameBoard[action[0]][action[1]].occupied = True
        customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = customPlayer.playerNum
        customPlayer.workers[0].row = action[0]
        customPlayer.workers[0].col = action[1]
        evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
        customGameBoard.gameBoard[action[2]][action[3]].level += 1
        # print('1: ', evalScore, action)
        if evalScore > maxScore:
            maxScore = evalScore
            bestMove = action
            bestWorker = 0
        customGameBoard.gameBoard[worker1row][worker1col].occupied = True
        customGameBoard.gameBoard[action[0]][action[1]].occupied = False
        customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = None
        customGameBoard.gameBoard[action[2]][action[3]].level -= 1
        customPlayer.workers[0].row = worker1row
        customPlayer.workers[0].col = worker1col

    for action in depth1Worker2:
        customGameBoard.gameBoard[worker2row][worker2col].occupied = False
        customGameBoard.gameBoard[action[0]][action[1]].occupied = True
        customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = customPlayer.playerNum
        customGameBoard.gameBoard[action[2]][action[3]].level += 1
        customPlayer.workers[1].row = action[0]
        customPlayer.workers[1].col = action[1]
        evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
        # print('2: ', evalScore, action)
        if evalScore > maxScore:
            maxScore = evalScore
            bestMove = action
            bestWorker = 1
        customGameBoard.gameBoard[worker2row][worker2col].occupied = True
        customGameBoard.gameBoard[action[0]][action[1]].occupied = False
        customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = None
        customGameBoard.gameBoard[action[2]][action[3]].level -= 1
        customPlayer.workers[1].row = worker2row
        customPlayer.workers[1].col = worker2col
    print('BEST MOVE: ', bestMove)
    print('MAX SCORE: ', maxScore)
    return bestMove, bestWorker
