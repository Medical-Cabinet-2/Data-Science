from flask import Flask, request
import json
from .StrainAPI import Strainer

def create_app():
    app = Flask(__name__)

    api = Strainer()


    @app.route('/')
    def root():
        """Default route, doesnt do anything"""
        msg = """
        <pre>
        Default route for the api\n

        Use /search to determine a strain for the user
        pass a json object with the data and it will return
        a json object with the result.
        As of 10:53 AM lambda time, the /search function
        will accept an input in the form of a json payload
        in the form of {'input': (int)} and return a json
        payload in the form of {'id': (int)+1}. Integration
        of the actual ML Algorithm is in progress and should
        be completed by the end of the day (01/08/2020)
        </pre>
        """
        return msg
    
    @app.route('/search', methods=['POST'])
    def search():
        """Useful route, calls the get_strain method"""
        data = json.loads(request.get_json())
        result = api.get_strain(data)
        return json.dumps({'id':result[0]})

    return app
