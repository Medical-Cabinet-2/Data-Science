"""
This library interfaces with the pickled model.
Using predictor:
"""

# Path and File Libraries
import os
import pickle

# Data Transformation Libraries
import pandas as pd
import numpy as np
import spacy

from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors



# Initialize parameters and spacy from __init__.py



###################
##BUILD PREDICTOR##
###################
class Predictor():
    def __init__(self,user_input_text=" ",size=5):
        self.nlp = spacy.load("en_core_web_md")
        
    def predict(self,user_input_text="",size=5):
        df = self.load_data()
        print("---b4")
        df_clean = self.preprocess(df)
        X,y = self.split_data(df_clean)
        
        # create tokenizer object
        self.tokenizer = Tokenizer(self.nlp.vocab)
        text = df_clean["combined_text"]
     
        predictions_text = self.transform_fit(text,user_input_text,size)
        return predictions_text

    def load_data(self):
        url='https://raw.githubusercontent.com/DNason1999/simple_repository/master/df_merged.csv'
        df = pd.read_csv(url)
        return df
    
    def preprocess(self,df):
        df['combined_text'] = df.Strain + ' ' + df.Type + ' ' + df.flavors + ' ' + df.Description + ' ' + df.positive + ' ' +    df.negative + ' ' + df.medical
        # Removing punctuations from our string
        df["combined_text"] = df['combined_text'].str.replace('[^\w\s]',' ')
        
        # Creating an index
        df.reset_index(level=0, inplace=True)
        
        for desc in df['combined_text']:
              if desc == 'None':
                desc = np.nan
        
        df = df.dropna()
        
        return df
    
    
    def split_data(self,df):
        # We set our features as description, and target as strain.  
        # Create a mass text.

        features = ['combined_text'] # expanding the features medical + flavors
        target = 'Strain'

        X = df[features]
        y = df[[target]]
    
        return X,y
    
    def tokenize(self,doc):
        """Return the tokens"""
        return [token.text for token in self.tokenizer(doc)]

    def get_lemmas(self,text):
        """Return the Lemmas"""
        lemmas = []
        doc = self.nlp(text)
    
        for token in doc: 
            if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_!= 'PRON'):
                lemmas.append(token.lemma_)
    
        return lemmas
    
    def transform_fit(self,text,user_input_text,size):
        # Instantiate vectorizer object
        tfidf = TfidfVectorizer(tokenizer=self.get_lemmas, min_df=0.025, max_df=.98, ngram_range=(1,2))

        # Create a vocabulary and get word counts per document
        dtm = tfidf.fit_transform(text) # Similiar to fit_predict

        # Get feature names to use as dataframe column headers
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
        # Fit on TF-IDF Vectors
        nn  = NearestNeighbors(n_neighbors=size, algorithm='ball_tree')
        nn.fit(dtm)

        user_input = user_input_text

        vec_user_input = tfidf.transform(user_input)
        a, strain = nn.kneighbors(vec_user_input.todense())
        
        recommended_strains = [df['combined_text'][n] for n in strain]
        
        return recommended_strains
    