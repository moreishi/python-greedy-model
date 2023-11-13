from pycaret.classification import *
from Species import Species
from Trainer import Trainer

class Model(object):

    modelName = None
    modelClass = None
    modelClasses = []
    models = []
    modelExperiment = None
    ModelTrainer = None

    def loadModel(self):
        self.modelExperiment = ClassificationExperiment()

        for idx, model in enumerate([member.value for member in Trainer]):
            self.modelClasses.append(self.modelExperiment.load_model(f'model/model_{model}'))

    def predictNext(self, data:any):
        
        norm = []

        for i in self.modelClasses:
            result = self.modelExperiment.predict_model(i, data, verbose=False)
            norm.append({'prediction_id': result['prediction_label'][0],
                    'prediction_score': result['prediction_score'][0], 
                    'prediction_specie': Species(int(result['prediction_label'][0])).name})
            
        return norm