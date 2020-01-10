# Path and File Libraries
import pickle
import os
import pandas as pd
import numpy as np
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer

###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self):    
        # Load in the pickled model
        self.nn = pickle.load(open("./models/nn_1.pkl", "rb"))
        self.tfidf = pickle.load(open("./models/tfidf_1.pkl", "rb"))
        # self.pars = pickle.load(open("./models/pars.pkl", "rb"))
        # self.vocab = pickle.load(open("./models/vocab.pkl", "rb"))
        # self.idf = pickle.load(open("./models/idf.pkl", "rb"))
        # self.pars['tokenizer']=get_lemmas
        # self.tfidf = TfidfVectorizer(self.pars)
        # self.tfidf.vocabulary_ = self.vocab
        # self.tfidf.idf_ = self.idf
        #self.nn = pickle.load(open(os.getcwd()+"/StrainAPI/models/nn_1.pkl", "rb"))
        #self.tfidf = pickle.load(open(os.getcwd()+"/StrainAPI/models/tfidf_1.pkl", "rb"))

    def predict(self,user_input_text,size=5):
        # Create vector from request string
        request_vec = self.tfidf.transform([user_input_text])
        # Use knn model to calculate the top n strains
        # The recommendations are the top n nearest points (vectors) to the
        # vectorized request, based on the vectorized dataset (vocab).
        strain_ids = self.nn.kneighbors(request_vec.todense(), n_neighbors=size)[1][0]
        return strain_ids

def get_lemmas(text):
    """Return the Lemmas"""
    lemmas = []
    doc = nlp(text)

    for token in doc: 
        if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_!= 'PRON'):
            lemmas.append(token.lemma_)

    return lemmas
