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
        Default route for the api

        Use /search to determine a strain for the user
        pass a json object with the data and it will return
        a json object with the result. 
        """
        return msg
    
    @app.route('/search', methods=['POST'])
    def search():
        """Useful route, calls the get_strain method"""
        data = json.loads(request.get_json())
        result = api.get_strain(data['input'])
        print(result)
        return json.dumps({'id':result[0]})

    return app
