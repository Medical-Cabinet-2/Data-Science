from flask import Flask, request, render_template
import json
from StrainAPI.nlp_model import Predictor

def create_app():
    app = Flask(__name__)

    api = Predictor()

    @app.route('/')
    def root():
        """Default route, renders documentation.html"""
        return render_template('documentation.html')
    
    @app.route('/search.html')
    def s():
        """Renders the search function documentation"""
        return render_template('search.html')

    @app.route('/test.html')
    def t():
        """Renders the test file"""
        return render_template('test.html')
    
    @app.route('/search', methods=['POST'])
    def search():
        """Useful route, calls the get_strain method"""
        # Accesses the json payload from the http request
        data = json.loads(request.get_json())

        types = data['type']
        flavor= data['flavor']
        effects= data['effects']
        description = data['desc']
        in_size = 3

        user_text = types+" "+flavor+" "+effects+" "+description

        # Generate the result from the machine learning api
        result = api.predict(user_input_text=user_text, size= in_size)

        return json.dumps({'id':result[0]})

    return app
