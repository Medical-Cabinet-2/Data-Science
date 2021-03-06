# Path and File Libraries
import pickle
import os

###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self):    
        # Load in the pickled model
        #self.nn = pickle.load(open("./models/nn_1.pkl", "rb"))
        #self.tfidf = pickle.load(open("./models/tfidf_1.pkl", "rb"))
        self.nn = pickle.load(open(os.getcwd()+"/StrainAPI/models/nn_1.pkl", "rb"))
        self.tfidf = pickle.load(open(os.getcwd()+"/StrainAPI/models/tfidf_1.pkl", "rb"))

    def predict(self,user_input_text,size=5):
        # Create vector from request string
        request_vec = self.tfidf.transform([user_input_text])
        # Use knn model to calculate the top n strains
        # The recommendations are the top n nearest points (vectors) to the
        # vectorized request, based on the vectorized dataset (vocab).
        strain_ids = self.nn.kneighbors(request_vec.todense(), n_neighbors=size)[1][0]
        return strain_ids
