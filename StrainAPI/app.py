from flask import Flask, request, render_template
from StrainAPI.nlp_model import Predictor
from StrainAPI.models import DB, Strain
import pandas as pd

def create_app():
    app = Flask(__name__)

    # Create instance of the predictor class (handles loading of ML model)
    api = Predictor()

    # Add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Stop tracking modifications on sqlalchemy config
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

    @app.route('/getdata')
    def getdata():
        return Strain.query.all()

    @app.route('/refresh')
    def refresh():
        """Refreshes the SQL Database with the merged strain dataset"""
        # Define URL to strain data csv
        url = 'https://raw.githubusercontent.com/DNason1999/simple_repository/master/df_merged.csv'
        # Read the data to a dataframe
        df = pd.read_csv(url)
        # Create an index column
        df = df.reset_index()

        # emove all tables in the sql database
        DB.drop_all()
        # Insert dataframe into sql database as table 'Strain'
        df.to_sql(name='Strain', con=DB.engine, index=False)
        # Commit the database changes
        DB.session.commit()

        #Return 200 as a status reponsse
        return '200'
    
    @app.route('/search', methods=['GET'])
    def search():
        """Useful route, calls the predict method"""

        # Create a user_text string from the various inputs recieved
        user_text = str(
            request.args.get('type')+" "+
            request.args.get('flavor')+" "+
            request.args.get('effects')+" "+
            request.args.get('desc')
        )
        # Define the size request
        in_size = int(request.args.get('size'))

        # Generate the result from the machine learning api
        result = api.predict(user_input_text=user_text, size= in_size)

        # Retrieve the actual strain information from the database using
        # the get_strain method
        output = get_strain(result, in_size)

        # Return the formated output dict
        return output

    def get_strain(ids, size):
        # Create an empty dictionary to return
        results = {}

        # Loop through all IDs recieved from the predict function in search()
        for x,index in zip(ids, range(0,size)):
            # Create a base result with {"id":"x"} where x is the current strain index
            sub_result = {"id":str(x)}
            # Query the database for the strain index and add it to the dict
            sub_result['data'] = Strain.query.filter(Strain.index==int(x)).first().__repr__()
            # Add the sub_result to the main results dictionary
            results['{}'.format(index)] = sub_result

        # Return the results in a dictionary
        return results
            
    return app
