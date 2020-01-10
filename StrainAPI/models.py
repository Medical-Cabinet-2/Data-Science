from flask_sqlalchemy import SQLAlchemy
import pandas as pd

DB = SQLAlchemy()

class Strain(DB.Model):
    """Strain with details"""
    index = DB.Column(DB.Integer, primary_key=True)
    Strain = DB.Column(DB.Text, nullable=False)
    Type = DB.Column(DB.Text, nullable=False)
    Rating = DB.Column(DB.Float, nullable=True)
    Description = DB.Column(DB.Text, nullable=True)
    flavors = DB.Column(DB.Text, nullable=False)
    medical = DB.Column(DB.Text, nullable=False)
    positive = DB.Column(DB.Text, nullable=False)
    negative = DB.Column(DB.Text, nullable=False)

    def __repr__(self):
        output = {
            'id':self.index,
            'name':self.Strain,
            'type':self.Type,
            'rate':self.Rating,
            'desc':self.Description,
            'flavor':self.flavors,
            'medical':self.medical,
            'positive':self.positive,
            'negative':self.negative
        }
        return output
