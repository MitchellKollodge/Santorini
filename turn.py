class TurnTracker:
    def __init__(self):
        self.history = []


    def addToHistory(self, player, workerNum, moveFromRow, moveFromCol, moveToRow, moveToCol, buildRow, buildCol):
        self.history.append({'player': player, 'workerNum': workerNum, 'moveFromRow': moveFromRow, 'moveFromCol': moveFromCol, 'moveToRow': moveToRow, 'moveToCol': moveToCol, 'buildRow': buildRow, 'buildCol': buildCol})


    def popFromHistory(self):
        return self.history.pop()


    def showHistory(self):
        for entry in self.history:
            print(entry)
