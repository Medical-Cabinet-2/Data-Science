from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

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

