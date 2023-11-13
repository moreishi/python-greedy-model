import pandas as pd

from Species import Species

class Prints:

    features = []
    featuresHistory = []

    def __init__(self) -> None:
        pass

    def setFeatures(self, features):
        self.features = features
    
    def prediction_logic(self, prediction):
        
        words = []
        label_id = []

        count_vegies = 0
        
        df = pd.DataFrame(prediction).groupby('prediction_specie').mean().sort_values(by=['prediction_score'], ascending=False)
        prediction = df.values.tolist()

        for idx,i in prediction:
            if int(idx) in [1,2,3,4]:
                count_vegies += 1
            if count_vegies > 3:
                continue
            if int(idx) in [9, 10]:
                continue

            words.append({'label_id': int(idx), 'label': Species(int(idx)).name, 'score': i})
            label_id.append(int(idx))

        for item in words:
            print(f"{item['label'][:5]} \t SCORE: {round(item['score'] * 100, 2)}%")
        
        return label_id
    
    def set_veggies(self, prediction_list):
        
        veggies = [1, 2, 3, 4]
        data = prediction_list
        count = 0

        for idx, i in enumerate(prediction_list):
            if i in veggies:
                count += 1
                if count > 3:
                    del data[idx]

        return data
    
    def print_options(self):
        options = []
        for idx, item in enumerate(Species):
            if idx == 0:
                continue
            options.append(f"{idx} = {Species(idx).name}")
        print(f"OPTIONS: {options}")

    def numeric_to_alpha_prediction(self, data):
        words = []
        for item in data:
            words.append(Species(int(item)).name)

        if 'Salad' in words:
            words.remove('Salad')

        return words
    
    def print_features(self, features):
        current = []
        for idx, item in enumerate(features):
            current.append(Species(int(item)).name)
        print("PRINT FEATURES: ", current)
    
    
    