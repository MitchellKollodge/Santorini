import copy
import gameBoard
import node
from numpy import inf


def buildTree(curPlayerNum, players, currentGameBoard):
    customGameBoard = copyGameBoard(currentGameBoard)
    nextPlayerNum = 1 if curPlayerNum == 0 else 0
    customMaxPlayer = copy.deepcopy(players[curPlayerNum])
    customMinPlayer = copy.deepcopy(players[nextPlayerNum])
    rootNode = node.Node()

    for actionSet in getCombos(customGameBoard, customMaxPlayer):
        tempNode = setupNode(actionSet, rootNode)
        workerNum = actionSet[0]
        action = actionSet[1]
        performAction(customGameBoard, customMaxPlayer, workerNum, action)
        if customGameBoard.checkForWinner():
            tempNode.value = -999999
            tempNode.leafNode = True
            undoAction(customGameBoard, customMaxPlayer, workerNum, action, action[0], action[1])
            continue
        depth2 = getCombos(customGameBoard, customMinPlayer)
        if len(depth2) == 0:
            tempNode.value = -999999
            tempNode.leafNode = True
            undoAction(customGameBoard, customMaxPlayer, workerNum, action, action[0], action[1])
            continue
        for actionSet2 in depth2:
            tempNode2 = setupNode(actionSet2, tempNode)
            workerNum2 = actionSet2[0]
            action2 = actionSet2[1]
            performAction(customGameBoard, customMinPlayer, workerNum2, action2)
            if customGameBoard.checkForWinner():
                tempNode2.value = 999999
                tempNode2.leafNode = True
                undoAction(customGameBoard, customMinPlayer, workerNum2, action2, action2[0], action2[1])
                continue
            depth3 = getCombos(customGameBoard, customMaxPlayer)
            if len(depth3) == 0:
                tempNode2.value = 999999
                tempNode2.leafNode = True
                undoAction(customGameBoard, customMinPlayer, workerNum2, action2, action2[0], action2[1])
                continue
            for actionSet3 in depth3:
                tempNode3 = setupNode(actionSet3, tempNode2)
                workerNum3 = actionSet3[0]
                action3 = actionSet3[1]
                performAction(customGameBoard, customMaxPlayer, workerNum3, action3)
                if customGameBoard.checkForWinner():
                    tempNode3.value = -999999
                    tempNode3.leafNode = True
                    undoAction(customGameBoard, customMaxPlayer, workerNum3, action3, action3[0], action3[1])
                    continue
                depth4 = getCombos(customGameBoard, customMinPlayer)
                if len(depth4) == 0:
                    tempNode3.value = -999999
                    tempNode3.leafNode = True
                    undoAction(customGameBoard, customMaxPlayer, workerNum3, action3, action3[0], action3[1])
                    continue
                for actionSet4 in depth4:
                    tempNode4 = setupNode(actionSet4, tempNode3)
                    workerNum4 = actionSet4[0]
                    action4 = actionSet4[1]
                    performAction(customGameBoard, customMinPlayer, workerNum4, action4)
                    if customGameBoard.checkForWinner():
                        tempNode4.value = 999999
                        tempNode4.leafNode = True
                        undoAction(customGameBoard, customMinPlayer, workerNum4, action4, action4[0], action4[1])
                        continue
                    depth5 = getCombos(customGameBoard, customMaxPlayer)
                    if len(depth5) == 0:
                        tempNode4.value = 999999
                        tempNode4.leafNode = True
                        undoAction(customGameBoard, customMinPlayer, workerNum4, action4, action4[0], action4[1])
                        continue
                    tempNode4.value = customGameBoard.evaluateGameBoard(customMinPlayer.playerNum)
                    tempNode4.leafNode = True
                    undoAction(customGameBoard, customMinPlayer, workerNum4, action4, action4[0], action4[1])
                undoAction(customGameBoard, customMaxPlayer, workerNum3, action3, action3[0], action3[1])
            undoAction(customGameBoard, customMinPlayer, workerNum2, action2, action2[0], action2[1])
        undoAction(customGameBoard, customMaxPlayer, workerNum, action, action[0], action[1])
    return rootNode


def minimax(curNode, depth, isMaximizingPlayer, alpha, beta):
    if curNode.leafNode == True:
        if curNode.parentNode is not None and curNode.actionSet is not None:
            if curNode.parentNode.parentNode is not None and curNode.parentNode.actionSet is not None:
                if curNode.parentNode.parentNode.parentNode is not None and curNode.parentNode.parentNode.actionSet is not None:
                    if curNode.parentNode.parentNode.parentNode.parentNode is not None and curNode.parentNode.parentNode.parentNode.actionSet is not None:
                        return curNode.value, curNode.parentNode.parentNode.parentNode.actionSet
                    return curNode.value, curNode.parentNode.parentNode.actionSet
                return curNode.value, curNode.parentNode.actionSet
            return curNode.value, curNode.actionSet
    if isMaximizingPlayer == True:
        bestVal = -inf
        bestActionSet = []
        for childNode in curNode.childNodes:
            value = minimax(childNode, depth + 1, False, alpha, beta)
            if value[0] > bestVal:
                bestVal = value[0]
                bestActionSet = value[1]
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal, bestActionSet
    else:
        bestVal = +inf
        bestActionSet = []
        for childNode in curNode.childNodes:
            value = minimax(childNode, depth + 1, True, alpha, beta)
            if value[0] < bestVal:
                bestVal = value[0]
                bestActionSet = value[1]
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal, bestActionSet


def setupNode(actionSet, parentNode):
    newNode = node.Node()
    newNode.actionSet = actionSet
    newNode.parentNode = parentNode
    parentNode.childNodes.append(newNode)
    return newNode


def getCombos(myGameBoard, player):
    combosWorker0 = myGameBoard.getAllMoveAndBuildCombos(0, player.workers[0].row, player.workers[0].col)
    combosWorker1 = myGameBoard.getAllMoveAndBuildCombos(1, player.workers[1].row, player.workers[1].col)
    combos = combosWorker0 + combosWorker1
    return combos if len(combos) > 0 else []


def oneDeepBestAction(player, currentGameBoard):
    customPlayer = copy.deepcopy(player)
    customGameBoard = copyGameBoard(currentGameBoard)
    depth1Worker0 = customGameBoard.getAllMoveAndBuildCombos(0, player.workers[0].row, player.workers[0].col)
    depth1Worker1 = customGameBoard.getAllMoveAndBuildCombos(1, player.workers[1].row, player.workers[1].col)
    bestMove = []
    bestWorker = None
    maxScore = -9999
    for action in depth1Worker0:
        performAction(customGameBoard, customPlayer, 0, action[1])
        evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
        if evalScore > maxScore:
            maxScore = evalScore
            bestMove = action[1]
            bestWorker = 0
        undoAction(customGameBoard, customPlayer, 1, action[1], player.workers[0].row, player.workers[0].col)
    for action in depth1Worker1:
        performAction(customGameBoard, customPlayer, 1, action[1])
        evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
        if evalScore > maxScore:
            maxScore = evalScore
            bestMove = action[1]
            bestWorker = 1
        undoAction(customGameBoard, customPlayer, 1, action[1], player.workers[1].row, player.workers[1].col)
    print('BEST MOVE: ', bestMove)
    print('MAX SCORE: ', maxScore)
    return bestMove, bestWorker


def copyGameBoard(currentGameBoard):
    customGameBoard = gameBoard.GameBoard()
    for row in range(len(currentGameBoard.gameBoard)):
        for col in range(len(currentGameBoard.gameBoard[row])):
            customGameBoard.gameBoard[row][col] = copy.deepcopy(currentGameBoard.gameBoard[row][col])
    return customGameBoard


def undoAction(customGameBoard, customPlayer, workerNum, action, workerRow, workerCol):
    customGameBoard.gameBoard[customPlayer.workers[workerNum].row][customPlayer.workers[workerNum].col].occupied = True
    customGameBoard.gameBoard[action[0]][action[1]].occupied = False
    customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = None
    customGameBoard.gameBoard[action[2]][action[3]].level -= 1
    customPlayer.workers[workerNum].row = workerRow
    customPlayer.workers[workerNum].col = workerCol


def performAction(customGameBoard, customPlayer, workerNum, action):
    customGameBoard.gameBoard[customPlayer.workers[workerNum].row][customPlayer.workers[workerNum].col].occupied = False
    customGameBoard.gameBoard[customPlayer.workers[workerNum].row][customPlayer.workers[workerNum].col].occupyingPlayer = None
    customGameBoard.gameBoard[action[0]][action[1]].occupied = True
    customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = customPlayer.playerNum
    customGameBoard.gameBoard[action[2]][action[3]].level += 1
    customPlayer.workers[workerNum].row = action[0]
    customPlayer.workers[workerNum].col = action[1]
