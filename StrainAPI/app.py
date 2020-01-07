from flask import Flask, render_template, request
from .StrainAPI import strainer

def create_app():
    app = Flask(__name__)

    api = strainer('QsLigX4')

    @app.route('/')
    def root():
        """Base view."""
        
        return render_template('base.html')
    
    return app