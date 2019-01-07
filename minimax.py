import copy
import gameBoard
import node
from numpy import inf
import turn
from multiprocessing import Process
from multiprocessing import Pool


class MiniMax:
    def __init__(self):
        self.turnTracker = turn.TurnTracker()


    def branchBuilder(self, everything):
        rootNode = everything[0]
        actionSet = everything[1]
        customGameBoard = everything[2]
        customMaxPlayer = everything[3]
        customMinPlayer = everything[4]

        tempNode = self.setupNode(actionSet, rootNode)
        workerNum = actionSet[0]
        action = actionSet[1]
        self.performAction(customGameBoard, customMaxPlayer, workerNum, action)
        if customGameBoard.checkForWinner():
            tempNode.value = 9000
            tempNode.leafNode = True
            self.undoAction(customGameBoard, customMaxPlayer, workerNum)
            return
        depth2 = self.getCombos(customGameBoard, customMinPlayer)
        if len(depth2) == 0:
            tempNode.value = 9000
            tempNode.leafNode = True
            self.undoAction(customGameBoard, customMaxPlayer, workerNum)
            return
        for actionSet2 in depth2:
            tempNode2 = self.setupNode(actionSet2, tempNode)
            workerNum2 = actionSet2[0]
            action2 = actionSet2[1]
            self.performAction(customGameBoard, customMinPlayer, workerNum2, action2)
            if customGameBoard.checkForWinner():
                tempNode2.value = -9000
                tempNode2.leafNode = True
                self.undoAction(customGameBoard, customMinPlayer, workerNum2)
                continue
            depth3 = self.getCombos(customGameBoard, customMaxPlayer)
            if len(depth3) == 0:
                tempNode2.value = -9000
                tempNode2.leafNode = True
                self.undoAction(customGameBoard, customMinPlayer, workerNum2)
                continue
            for actionSet3 in depth3:
                tempNode3 = self.setupNode(actionSet3, tempNode2)
                workerNum3 = actionSet3[0]
                action3 = actionSet3[1]
                self.performAction(customGameBoard, customMaxPlayer, workerNum3, action3)
                if customGameBoard.checkForWinner():
                    tempNode3.value = 9000
                    tempNode3.leafNode = True
                    self.undoAction(customGameBoard, customMaxPlayer, workerNum3)
                    continue
                depth4 = self.getCombos(customGameBoard, customMinPlayer)
                if len(depth4) == 0:
                    tempNode3.value = 9000
                    tempNode3.leafNode = True
                    self.undoAction(customGameBoard, customMaxPlayer, workerNum3)
                    continue
                for actionSet4 in depth4:
                    tempNode4 = self.setupNode(actionSet4, tempNode3)
                    workerNum4 = actionSet4[0]
                    action4 = actionSet4[1]
                    self.performAction(customGameBoard, customMinPlayer, workerNum4, action4)
                    if customGameBoard.checkForWinner():
                        tempNode4.value = -9000
                        tempNode4.leafNode = True
                        self.undoAction(customGameBoard, customMinPlayer, workerNum4)
                        continue
                    depth5 = self.getCombos(customGameBoard, customMaxPlayer)
                    if len(depth5) == 0:
                        tempNode4.value = -9000
                        tempNode4.leafNode = True
                        self.undoAction(customGameBoard, customMinPlayer, workerNum4)
                        continue
                    tempNode4.value = customGameBoard.evaluateGameBoard(customMinPlayer.playerNum)
                    tempNode4.leafNode = True
                    self.undoAction(customGameBoard, customMinPlayer, workerNum4)
                self.undoAction(customGameBoard, customMaxPlayer, workerNum3)
            self.undoAction(customGameBoard, customMinPlayer, workerNum2)
        self.undoAction(customGameBoard, customMaxPlayer, workerNum)
        return tempNode


    def buildTree(self, curPlayerNum, players, currentGameBoard):
        customGameBoard = self.copyGameBoard(currentGameBoard)
        nextPlayerNum = 1 if curPlayerNum == 0 else 0
        customMaxPlayer = copy.deepcopy(players[curPlayerNum])
        customMinPlayer = copy.deepcopy(players[nextPlayerNum])
        rootNode = node.Node()

        depth1 = self.getCombos(customGameBoard, customMaxPlayer)

        processArgs = []
        for actionSet in depth1:
            processArgs.append([rootNode, actionSet, self.copyGameBoard(currentGameBoard), copy.deepcopy(players[curPlayerNum]), copy.deepcopy(players[nextPlayerNum])])

        p = Pool(len(processArgs))
        data = p.map(self.branchBuilder, processArgs)
        p.close()

        for tempNode in data:
            if tempNode is not None:
                rootNode.childNodes.append(tempNode)
                tempNode.parentNode = rootNode

        return rootNode


    def minimax(self, curNode, depth, isMaximizingPlayer, alpha, beta):
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
                value = self.minimax(childNode, depth + 1, False, alpha, beta)
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
                value = self.minimax(childNode, depth + 1, True, alpha, beta)
                if value[0] < bestVal:
                    bestVal = value[0]
                    bestActionSet = value[1]
                beta = min(beta, bestVal)
                if beta <= alpha:
                    break
            return bestVal, bestActionSet


    def setupNode(self, actionSet, parentNode):
        newNode = node.Node()
        newNode.actionSet = actionSet
        newNode.parentNode = parentNode
        parentNode.childNodes.append(newNode)
        return newNode


    def getCombos(self, myGameBoard, player):
        combosWorker0 = myGameBoard.getAllMoveAndBuildCombos(0, player.workers[0].row, player.workers[0].col)
        combosWorker1 = myGameBoard.getAllMoveAndBuildCombos(1, player.workers[1].row, player.workers[1].col)
        combos = combosWorker0 + combosWorker1
        return combos if len(combos) > 0 else []


    def oneDeepBestAction(self, player, currentGameBoard):
        customPlayer = copy.deepcopy(player)
        customGameBoard = self.copyGameBoard(currentGameBoard)
        depth1Worker0 = customGameBoard.getAllMoveAndBuildCombos(0, player.workers[0].row, player.workers[0].col)
        depth1Worker1 = customGameBoard.getAllMoveAndBuildCombos(1, player.workers[1].row, player.workers[1].col)
        bestMove = []
        bestWorker = None
        maxScore = -9999
        for action in depth1Worker0:
            self.performAction(customGameBoard, customPlayer, 0, action[1])
            evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
            if evalScore > maxScore:
                maxScore = evalScore
                bestMove = action[1]
                bestWorker = 0
            self.undoAction(customGameBoard, customPlayer, 1)
        for action in depth1Worker1:
            self.performAction(customGameBoard, customPlayer, 1, action[1])
            evalScore = customGameBoard.evaluateGameBoard(player.playerNum)
            if evalScore > maxScore:
                maxScore = evalScore
                bestMove = action[1]
                bestWorker = 1
            self.undoAction(customGameBoard, customPlayer, 1)
        print('BEST MOVE: ', bestMove)
        print('MAX SCORE: ', maxScore)
        return bestMove, bestWorker


    def copyGameBoard(self, currentGameBoard):
        customGameBoard = gameBoard.GameBoard()
        for row in range(len(currentGameBoard.gameBoard)):
            for col in range(len(currentGameBoard.gameBoard[row])):
                customGameBoard.gameBoard[row][col] = copy.deepcopy(currentGameBoard.gameBoard[row][col])
        return customGameBoard


    def undoAction(self, customGameBoard, customPlayer, workerNum):
        previousPos = self.turnTracker.popFromHistory()
        customGameBoard.gameBoard[previousPos['moveFromRow']][previousPos['moveFromCol']].occupied = True
        customGameBoard.gameBoard[previousPos['moveFromRow']][previousPos['moveFromCol']].occupyingPlayer = customPlayer.playerNum
        customGameBoard.gameBoard[previousPos['moveToRow']][previousPos['moveToCol']].occupied = False
        customGameBoard.gameBoard[previousPos['moveToRow']][previousPos['moveToCol']].occupyingPlayer = None
        customGameBoard.gameBoard[previousPos['buildRow']][previousPos['buildCol']].level -= 1
        customPlayer.workers[workerNum].row = previousPos['moveFromRow']
        customPlayer.workers[workerNum].col = previousPos['moveFromCol']


    def performAction(self, customGameBoard, customPlayer, workerNum, action):
        self.turnTracker.addToHistory(customPlayer, workerNum, customPlayer.workers[workerNum].row, customPlayer.workers[workerNum].col, action[0], action[1], action[2], action[3])
        customGameBoard.gameBoard[customPlayer.workers[workerNum].row][customPlayer.workers[workerNum].col].occupied = False
        customGameBoard.gameBoard[customPlayer.workers[workerNum].row][customPlayer.workers[workerNum].col].occupyingPlayer = None
        customGameBoard.gameBoard[action[0]][action[1]].occupied = True
        customGameBoard.gameBoard[action[0]][action[1]].occupyingPlayer = customPlayer.playerNum
        customGameBoard.gameBoard[action[2]][action[3]].level += 1
        customPlayer.workers[workerNum].row = action[0]
        customPlayer.workers[workerNum].col = action[1]
