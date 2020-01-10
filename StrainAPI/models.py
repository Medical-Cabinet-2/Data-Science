from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

DB.drop_all()
DB.create_all()

url = 'https://raw.githubusercontent.com/DNason1999/simple_repository/master/df_merged.csv'
df = pd.read_csv(url)

df.to_sql('Strain', con=DB)

class Strain(DB.Model):
    """Strain with details"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    strain = DB.Column(DB.Text, nullable=False)
    types = DB.Column(DB.Text, nullable=False)
    flavors = DB.Column(DB.Text, nullable=False)
    medical = DB.Column(DB.Text, nullable=False)
    positive = DB.Column(DB.Text, nullable=False)
    negative = DB.Column(DB.Text, nullable=False)

    def __repr__(self):
        output = {
            'id':self.id,
            'name':self.strain,
            'type':self.types,
            'flavor':self.flavors,
            'medical':self.medical,
            'positive':self.positive,
            'negative':self.negative
        }
        return output

