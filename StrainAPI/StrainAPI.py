import requests
import pickle
from sklearn

class Strainer():
    def __init__(self, key):
        self.filename = '(INSERT FILENAME)'
        self.model = pickle.load(open(self.filename, 'rb'))

    def get_strain(self, search_type, query):
        model.predict

        print(url)
        return requests.request("GET", url)