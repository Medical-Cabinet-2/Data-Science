from flask import Flask, request, render_template
import json
from .StrainAPI import Strainer

def create_app():
    app = Flask(__name__)

    api = Strainer()

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
        data = json.loads(request.get_json())
        result = api.get_strain(data)
        return json.dumps({'id':result[0]})

    return app
