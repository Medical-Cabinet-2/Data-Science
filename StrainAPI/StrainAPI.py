import requests
import pickle
from sklearn.linear_model import LinearRegression
import os

class Strainer():
    def __init__(self):
        print(os.getcwd())
        print(os.listdir())
        self.filename = os.getcwd()+'/StrainAPI/models/dummy_linear_regression.pkl'
        self.model = pickle.load(open(self.filename, 'rb'))

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
