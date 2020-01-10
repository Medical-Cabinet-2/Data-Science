from flask import Flask, request, render_template, jsonify
import json
from StrainAPI.nlp_model import Predictor
from StrainAPI.models import DB, Strain
import pandas as pd

def create_app():
    app = Flask(__name__)

    #Create instance of the predictor class (handles loading of ML model)
    api = Predictor()

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    

    @app.route('/')
    def root():
        """Default route, renders documentation.html"""
        return render_template('documentation.html')
    
    @app.route('/search.html')
    def s():
        """Renders the search function documentation"""
        return render_template('search.html')

    @app.route('/refresh')
    def refresh():
        url = 'https://raw.githubusercontent.com/DNason1999/simple_repository/master/df_merged.csv'
        df = pd.read_csv(url)
        df = df.reset_index().rename({'index':'id'})

        DB.drop_all()

        df.to_sql(name='Strain', con=DB.engine, index=False)

        DB.session.commit()

        return '200'
    
    @app.route('/search', methods=['GET'])
    def search():
        """Useful route, calls the get_strain method"""
        # Accesses the json payload from the http request

        user_text = str(
            request.args.get('type')+" "+
            request.args.get('flavor')+" "+
            request.args.get('effects')+" "+
            request.args.get('desc')
        )
        in_size = int(request.args.get('size'))

        # Generate the result from the machine learning api
        result = api.predict(user_input_text=user_text, size= in_size)

        output = get_strain(result, in_size)

        return output

    def get_strain(ids, size):
        results = {}
        for x,index in zip(ids, range(0,size)):
            sub_result = {"id":str(x)}
            sub_result['data'] = Strain.query.filter(Strain.index==int(x)).first().__repr__()
            results['{}'.format(index)] = sub_result
        
        return results
            
    return app
