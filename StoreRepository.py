from Store import Store

class StoreRepository(Store):

    def __init__(self) -> None:
        pass

    def getTotalRounds(self):
        return self.TOTAL_WIN + self.TOTAL_LOSS

    def getWinPercent(self):
        return round(0 if self.TOTAL_WIN == 0 else (self.TOTAL_WIN / self.getTotalRounds()) * 100, 2)
    
    def getLossPercent(self):
        return round(0 if self.TOTAL_LOSS == 0 else (self.TOTAL_LOSS / self.getTotalRounds()) * 100, 2)
    