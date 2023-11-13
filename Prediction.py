from pycaret.datasets import get_data
from pycaret.classification import *
from Species import Species
from Model import Model
from FileService import FileService
from Prints import Prints
from StoreService import StoreService
from StoreRepository import StoreRepository
from StoreDTO import StoreDTO
from Menu import Menu


class Prediction(StoreService, StoreRepository, Model, object):

    fileName = ''
    fileNameWithExt = ''

    PrintsService = None

    def __init__(self, *args):
        pass
        self.PrintsService = Prints()
        self.PrintsService.print_options()
    
    def input_features(self):
        data = input('ENTER FEATURES: ')
        self.features = data.split()
        if len(self.features) < 8:
            print("INVALID INPUT FEATURES")
            self.input_features()

    def print_features(self):
        self.PrintsService.print_features(self.features)

    def input_prediction(self):
        
        self.PrintsService.print_options()
        
        winning = input("ENTER WINNING RESULT: ")
        
        if winning == "": self.input_prediction()
        if winning in [member.value for member in Menu]:
            
            if winning == Menu("RESET").value:
                self.features = []
                print(self.features)
                self.input_prediction()
            
            elif winning == Menu("BACK").value:
                self.features = self.featuresHistory.copy()
                print(self.features)
                self.input_prediction()

            elif winning == Menu("QUIT").value:
                quit()


        
        self.featuresHistory = self.features.copy()
        self.features.append(winning)

        if len(self.features) > 24:
            self.features.pop(0)
        else:
            print(len(self.features))
            print(self.features)
            self.input_prediction()

        row = self.features.copy()
        
        prev_rediction = self.prediction_list.copy()

        self.saveToFile(row, self.fileNameWithExt)
        self.predictFeature() # starts predicting

        # update stats
        self.setStat(Species(int(winning)).name, 1)
        self.print_features()

        setVeggies = self.PrintsService.set_veggies(self.prediction_list)
        self.set_prediction_list(setVeggies)
        self.PrintsService.numeric_to_alpha_prediction(setVeggies)

        self.setWinLossStat(winning, prev_rediction)
        
        # get win and percentage
        print(f"\n")

        predict_logic = Prints()
        self.prediction_list =  predict_logic.prediction_logic(self.prediction)
        
        print(f"PREVIOUS WINNING RESULT: {Species(int(winning)).name}")

        self.setVeggieHitCount(winning, self.prediction_list)
        print(f"\n")

        
        self.resetStatValue(Species(int(winning)).name, 0)
        for idx in range(10): self.setStat(Species(int(idx)).name, 1)
        self.printStats()

        self.input_prediction()
    

    def predictFeature(self):
        data = self.predictNext(data=get_data(self.fileName))
        for item in data:
            self.prediction.append(item)
    
    def set_prediction_list(self, data):
        self.prediction_list = data.copy()

    def printStats(self):

        TOTAL_ROUNDS = self.getTotalRounds()
        WIN_PERCENT = self.getWinPercent()
        LOSS_PERCENT = self.getLossPercent()

        print(f"TOTAL ROUNDS: {TOTAL_ROUNDS}")
        print(f"TOTAL WIN: {self.TOTAL_WIN} {WIN_PERCENT}%, \t TOTAL LOSS: {self.TOTAL_LOSS} {LOSS_PERCENT}%")
        print(f"WINNING STREAK: {self.STREAK_WIN}, \t LOSING STREAK: {self.STREAK_LOSS}")
        print(f"VEGGIE STRIKE: {self.VEGE_STRIKE}, \t VEGGIE SPARE: {self.VEGE_SPARE}")
        print(f"\n")
        print(f"VEGGIE TOP: {self.VEGE_TOP}, \t VEGGIE MID: {self.VEGE_MID}, \t VEGGIE BOT: {self.VEGE_BOT}")
        print(f"\n")
        print(f"HOT_DOG: {self.HOT_DOG}, BBQ: {self.BBQ}, HAM: {self.HAM}, STEAK: {self.STEAK}")
        print(f"TOMATO: {self.TOMATO}, CABBAGE: {self.CABBAGE}, CORN: {self.CORN}, CARROT: {self.CARROT}")
        print(f"\n")
