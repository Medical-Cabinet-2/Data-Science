from flask import Flask, request
import json
from .StrainAPI import Strainer
from .models import Strain

def create_app():
    app = Flask(__name__)

    api = Strainer()


    @app.route('/')
    def root():
        """Default route, doesnt do anything"""
        msg = """
        Default route for the api\n

        Use /search to determine a strain for the user
        pass a json object with the data and it will return
        a json object with the result.\n
        As of 10:53 AM lambda time, the /search function\n
        will accept an input in the form of a json payload\n
        in the form of {'input': (int)} and return a json\n
        payload in the form of {'id': (int)+1}. Integration\n
        of the actual ML Algorithm is in progress and should\n
        be completed by the end of the day (01/08/2020)
        """
        return msg

    @app.route('/search', methods=['POST'])
    def search():
        """Useful route, calls the get_strain method"""
        data = json.loads(request.get_json())
        result = api.get_strain(data)
        return json.dumps({'id':result[0]})

    return app

#a function to use ML Model in puts and return the row information

def strain_sql(indices):
    """this function should take indices (the five from the ML model) \n
    and return the information contained in those rows"""
    strain = Strain.query.filter(Strain.index == index).one()#one index
    strains = Strain.query.filter(Strain.index.in_(indices)).one()#for all indices
    return strains



if __name__ == '__main__':
    app.run()
