import requests
import pickle



class Strainer():
    def __init__(self):
        self.model = Predictor()

    def get_strain(self, data):
        """
        Using machine learning model to predict a strain for a user
        :param data: The data to be used to predict a strain
        """
        vals = []
        for val in data.values():
            vals.append(val)
        prediction = self.model.predict([vals])

        return prediction
