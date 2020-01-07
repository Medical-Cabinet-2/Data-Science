import requests
import pickle
from sklearn.linear_model import LinearRegression

class Strainer():
    def __init__(self):
        self.filename = "dummy_linear_regression.pkl"
        self.model = pickle.load(open(self.filename, 'rb'))

    def get_strain(self, data):
        """
        Using machine learning model to predict a strain for a user
        :param data: The data to be used to predict a strain
        """
        prediction = self.model.predict(data)

        return prediction
