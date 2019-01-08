import tile
import turn


class GameBoard:
    def __init__(self):
        self.gameBoard = self.createBaseGameBoard()
        self.turnTracker = turn.TurnTracker()

    # Tests written
    def buildLevel(self, player, row, col):
        if ([row, col] in self.getNeighboringPositions(player.workers[0].row, player.workers[0].col) or
                [row, col] in self.getNeighboringPositions(player.workers[1].row, player.workers[1].col)):
            if self.verifyValidBuild(row, col):
                self.gameBoard[row][col].level += 1
                return True
        return False

    def checkForWinner(self):
        for row in range(len(self.gameBoard)):
            for col in range(len(self.gameBoard[row])):
                if self.gameBoard[row][col].level == 3 and self.gameBoard[row][col].occupied == True:
                    return True
        return False

    def createBaseGameBoard(self):
        gameBoard = [[tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
                     [tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
                     [tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
                     [tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()],
                     [tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile(), tile.Tile()]]
        return gameBoard

    def evaluateGameBoard(self, playerNum):
        heightValue = [0, 300, 900, 9000]
        value = 0
        for row in range(len(self.gameBoard)):
            for col in range(len(self.gameBoard[row])):
                if self.gameBoard[row][col].occupyingPlayer == playerNum:
                    value += heightValue[self.gameBoard[row][col].level]
                elif self.gameBoard[row][col].occupied:
                    value -= heightValue[self.gameBoard[row][col].level]
        return value


    def getAllMoveAndBuildCombos(self, workerNum, row, col):
        combos = []
        appendCombos = combos.append
        getValidBuildsTest = self.getValidBuilds
        allValidMoves = self.getValidMoves(row, col)
        for move in allValidMoves:
            validBuilds = getValidBuildsTest(move[0], move[1])
            validBuilds.append([row, col])
            for build in validBuilds:
                appendCombos([workerNum, move + build])
        return combos

# Tests written
    def getNeighboringPositions(self, row, col):
        possiblePositions = []
        appendPos = possiblePositions.append
        if self.validatePosition(row - 1, col):
            appendPos([row - 1, col])
        if self.validatePosition(row - 1, col + 1):
            appendPos([row - 1, col + 1])
        if self.validatePosition(row - 1, col - 1):
            appendPos([row - 1, col - 1])
        if self.validatePosition(row, col + 1):
            appendPos([row, col + 1])
        if self.validatePosition(row, col - 1):
            appendPos([row, col - 1])
        if self.validatePosition(row + 1, col):
            appendPos([row + 1, col])
        if self.validatePosition(row + 1, col + 1):
            appendPos([row + 1, col + 1])
        if self.validatePosition(row + 1, col - 1):
            appendPos([row + 1, col - 1])
        return possiblePositions


# Tests written
# Tried list comprehension, but was slower.
    def getValidBuilds(self, row, col):
        validBuilds = []
        appendBuilds = validBuilds.append
        verifyValidBuild = self.verifyValidBuild
        neighboringPositions = self.getNeighboringPositions(row, col)
        for pos in neighboringPositions:
            if verifyValidBuild(pos[0], pos[1]):
                appendBuilds(pos)
        return validBuilds


# Tests written
# Tried list comprehension, but was slower.
    def getValidMoves(self, row, col):
        validMoves = []
        appendMoves = validMoves.append
        validateMoveLevel = self.validateMoveLevel
        checkForCollision = self.workersWillCollide
        neighboringPositions = self.getNeighboringPositions(row, col)
        for pos in neighboringPositions:
            if validateMoveLevel(row, col, pos[0], pos[1]) and not checkForCollision(pos[0], pos[1]):
                appendMoves(pos)
        return validMoves


    # Tests written
    def moveWorker(self, player, workerNum, row, col):
        if [row, col] in self.getNeighboringPositions(player.workers[workerNum].row, player.workers[workerNum].col):
            if self.workersWillCollide(row, col) == False and self.validateMoveLevel(player.workers[workerNum].row,
                                                                                     player.workers[workerNum].col, row,
                                                                                     col):
                player.previousPositionWorker.row = player.workers[workerNum].row
                player.previousPositionWorker.col = player.workers[workerNum].col
                player.workers[workerNum].row = row
                player.workers[workerNum].col = col
                player.lastMovedWorker = workerNum
                self.gameBoard[player.previousPositionWorker.row][player.previousPositionWorker.col].occupied = False
                self.gameBoard[row][col].occupied = True
                self.gameBoard[player.previousPositionWorker.row][
                    player.previousPositionWorker.col].occupyingPlayer = None
                self.gameBoard[row][col].occupyingPlayer = player.playerNum
                return True
        return False

    # Tests written
    def placeInitialWorker(self, player, workerNum, row, col):
        if self.workersWillCollide(row, col) == False and self.validatePosition(row, col):
            player.previousPositionWorker.row = row
            player.previousPositionWorker.col = col
            player.workers[workerNum].row = row
            player.workers[workerNum].col = col
            player.lastMovedWorker = workerNum
            self.gameBoard[row][col].occupied = True
            self.gameBoard[row][col].occupyingPlayer = player.playerNum
            self.turnTracker.addToHistory(player, workerNum, -1, -1, row, col, None, None)
            return True
        return False

    def printGameBoardLevels(self):
        for rowIndex in range(len(self.gameBoard)):
            rowStr = ''
            for colIndex in range(len(self.gameBoard[rowIndex])):
                rowStr += str(self.gameBoard[rowIndex][colIndex].level) + '  '
            print(rowStr)
        print()

    def printGameBoardWorkers(self, oldRow, oldCol, players):
        player1Workers = players[0].workers
        player2Workers = players[1].workers
        for rowIndex in range(len(self.gameBoard)):
            rowStr = ''
            for colIndex in range(len(self.gameBoard[rowIndex])):
                if self.gameBoard[rowIndex][colIndex].occupied:
                    if (player1Workers[0].row == rowIndex and player1Workers[0].col == colIndex):
                        rowStr += '\033[92m' + 'True 00 ' + '\033[0m'  # Green
                    elif (player1Workers[1].row == rowIndex and player1Workers[1].col == colIndex):
                        rowStr += '\033[92m' + 'True 01 ' + '\033[0m'  # Green
                    elif (player2Workers[0].row == rowIndex and player2Workers[0].col == colIndex):
                        rowStr += '\033[92m' + 'True 10 ' + '\033[0m'  # Green
                    else:
                        rowStr += '\033[92m' + 'True 11 ' + '\033[0m'  # Green
                elif rowIndex == oldRow and colIndex == oldCol:
                    if players[0].previousPositionWorker.row == oldRow and players[
                        0].previousPositionWorker.col == oldCol:
                        rowStr += '\033[33m' + 'False0  ' + '\033[0m'  # Yellow
                    else:
                        rowStr += '\033[33m' + 'False1  ' + '\033[0m'  # Yellow
                else:
                    rowStr += 'False   '
            print(rowStr)
        print()

    # Tests written
    def validateMoveLevel(self, oldRow, oldCol, newRow, newCol):
        currentWorkerLevel = self.gameBoard[oldRow][oldCol].level
        moveLevel = self.gameBoard[newRow][newCol].level
        return 0 <= moveLevel < 4 and moveLevel - currentWorkerLevel <= 1

    # Tests written
    def validatePosition(self, row, col):
        return 0 <= row <= 4 and 0 <= col <= 4

    # Tests written
    def verifyValidBuild(self, row, col):
        return self.gameBoard[row][col].level < 4 and not self.gameBoard[row][col].occupied

    # Tests written
    def workersWillCollide(self, row, col):
        return self.gameBoard[row][col].occupied
