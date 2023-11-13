from Store import Store
from FileService import FileService

class StoreService(Store):

    def __init__(self) -> None:
        pass

    def increaseWin(self, num):
        self.TOTAL_WIN += num

    def increaseLoss(self, num):
        self.TOTAL_LOSS += num

    def setStat(self, OPTION: str, num):

        match OPTION:
            case 'STEAK':
                self.STEAK += num
            case 'HOT_DOG':
                self.HOT_DOG += num
            case 'BBQ':
                self.BBQ += num
            case 'HAM':
                self.HAM += num
            case 'TOMATO':
                self.TOMATO += num
            case 'CABBAGE':
                self.CABBAGE += num
            case 'CORN':
                self.CORN += num
            case 'CARROT':
                self.CARROT += num

    def resetStatValue(self, OPTION: str, num):

        match OPTION:
            case 'STEAK':
                self.STEAK = num
            case 'HOT_DOG':
                self.HOT_DOG = num
            case 'BBQ':
                self.BBQ = num
            case 'HAM':
                self.HAM = num
            case 'TOMATO':
                self.TOMATO = num
            case 'CABBAGE':
                self.CABBAGE = num
            case 'CORN':
                self.CORN = num
            case 'CARROT':
                self.CARROT = num

    def setStreakCount(self, result='WIN'):
            if result == 'WIN':
                self.STREAK_LOSS = 0
                self.STREAK_WIN += 1
            else:
                self.STREAK_LOSS += 1
                self.STREAK_WIN = 0

    def setWinLossCount(self, win=True):
        if win == True:
            self.TOTAL_WIN += 1
        else:
            self.TOTAL_LOSS += 1

    def setVeggieHitCount(self, WIN, prediction_list):
        veggies = [1,2,3,4]
        data = []

        WIN = int(WIN)

        for idx, item in enumerate(prediction_list):
            if item in veggies:
                data.append(item)
        
        if WIN in data:
            
            if data.index(WIN) in [0,1]:
               self.VEGE_STRIKE += 1
            else:
                self.VEGE_SPARE += 1

            if data.index(WIN) == 0:
                self.VEGE_TOP += 1
            if data.index(WIN) == 1:
                self.VEGE_MID += 1
            if data.index(WIN) == 2:
                self.VEGE_BOT += 1

    def setWinLossStat(self, winning, prev_rediction):

        if (int(winning)) in prev_rediction:
            self.setWinLossCount(True)
            self.setStreakCount('WIN')
        else:
            self.setWinLossCount(False)
            self.setStreakCount('LOSS')

    def saveToFile(self, row, fileNameWithExt):
        file = FileService(fileNameWithExt)
        file.setColumns(24)
        file.setData(row)
        file.write()