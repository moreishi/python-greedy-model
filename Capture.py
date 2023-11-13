from StoreService import StoreService
from StoreRepository import StoreRepository
from StoreDTO import StoreDTO

from Prints import Prints

class Capture(StoreRepository, StoreService):
    
    PrintsService = None

    fileName = ''
    fileNameWithExt = ''

    SELECT_RESET = 'r' # RESET ALL
    SELECT_QUIT = 'q' # QUIT APP
    SELECT_BACK = 'b' # RESET BACK
    
    def __init__(self) -> None:
        pass
        self.PrintsService = Prints()
    
    def run(self):
        self.PrintsService.print_options()
        self.input_features()
        self.input_capture()

    def input_features(self):
        data = input('ENTER FEATURES: ')
        self.features = data.split()
        if len(self.features) < 8:
            print("INVALID INPUT FEATURES")
            self.input_features()

    def input_capture(self):

        winning = input("ENTER WINNING RESULT: ")
    
        if winning == "": self.input_capture()
        if winning in [self.SELECT_BACK, self.SELECT_QUIT, self.SELECT_RESET]:
            
            if winning == self.SELECT_RESET:
                self.features = []
                print(self.features)
                self.input_capture()
            
            elif winning == self.SELECT_BACK:
                self.features = self.featuresHistory.copy()
                print(self.features)
                self.input_capture()

            elif winning == self.SELECT_QUIT:
                quit()
        
        if winning == "s": 
            self.saveToFile(self.features, self.fileNameWithExt)
            print(f"Saving..")
            self.input_capture()

        # write to features
        self.features.append(winning)

        print(self.features)
        self.input_capture()

    
    
capture = Capture()
capture.fileNameWithExt = 'capture.csv'
capture.run()
