from flask import Flask, request, jsonify
from .StrainAPI import strainer

def create_app():
    app = Flask(__name__)

    api = Strainer()

    @app.route('/')
    def root():
        return 'Root stuff'
    
    @app.route('/search', methods=['POST'])
    def search():
        data = request.get_json()

        return data

    return app