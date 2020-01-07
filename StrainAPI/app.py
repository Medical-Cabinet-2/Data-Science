from flask import Flask, render_template, request
from .StrainAPI import strainer

def create_app():
    app = Flask(__name__)

    api = strainer('QsLigX4')

    @app.route('/')
    def root():
        """Base view."""
        
        return 'Root stuff'
    
    @app.route('/search', methods=['POST'])
    def search():
        return 'Search Function'

    return app