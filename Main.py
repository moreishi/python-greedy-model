from Prediction import Prediction

class Main():

    def __init__(self) -> None:
        pass
        self.prediction()

    def prediction(self):

        # init
        predict = Prediction()
        predict.fileName = 'predict'
        predict.fileNameWithExt = 'predict.csv'

        # model
        predict.loadModel()

        # set dataset
        predict.input_features()
        predict.print_features()
        predict.input_prediction()


app = Main()