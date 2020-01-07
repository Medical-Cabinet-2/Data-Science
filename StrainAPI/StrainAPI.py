import requests
import pickle
from sklearn.linear_model import LinearRegression

class Strainer():
    def __init__(self):
        url = 'https://github.com/Medical-Cabinet-2/Data-Science/blob/DNason/StrainAPI/Dummy_linear_regression.pkl?raw=true'
        self.model = pickle.loads(requests.request("GET", url).content)

    def get_strain(self, data):
        """
        Using machine learning model to predict a strain for a user
        :param data: The data to be used to predict a strain
        """
        prediction = self.model.predict([[data]])

        return prediction
