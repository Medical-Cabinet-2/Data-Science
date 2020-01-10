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
    
    @app.route('/search', methods=['GET'])
    def search():
        """Useful route, calls the get_strain method"""
        # Accesses the json payload from the http request

        types = request.args.get('type')
        flavor= request.args.get('flavor')
        effects = request.args.get('effects')
        description = request.args.get('desc')
        in_size = int(request.args.get('size'))

        user_text = types+" "+flavor+" "+effects+" "+description

        # Generate the result from the machine learning api
        result = api.predict(user_input_text=user_text, size= in_size)
        print(result)

        return json.dumps({'id':result[0]})
            
    return app
