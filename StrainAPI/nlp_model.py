# Path and File Libraries
import pickle
import os
import pandas as pd
import numpy as np
import spacy

from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

###################
##BUILD PREDICTOR##
###################
class Predictor():
    def __init__(self):
        # Load in the pickled model
        print(os.getcwd())
        self.nn = pickle.load(open("./models/nn_1.pkl", "rb"))
        self.tfidf = pickle.load(open("./models/tfidf_1.pkl", "rb"))

    def predict(self,user_input_text,size=5):
        # Create vector from request string
        request_vec = self.tfidf.transform(user_input_text)
        # Use knn model to calculate the top n strains
        # The recommendations are the top n nearest points (vectors) to the
        # vectorized request, based on the vectorized dataset (vocab).
        strain_ids = self.nn.kneighbors(request_vec.todense(), n_neighbors=size)[1][0]
        return strain_ids
        
    