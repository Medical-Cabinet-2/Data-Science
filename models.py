from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


DB = SQLAlchemy()

class Strain(DB.Model):
    """Strain with details"""
    index = DB.Column(DB.BigInteger, primary_key=True)
    Strain = DB.Column(DB.Text, nullable=False)
    flavors = DB.Column(DB.Text, nullable=False)
    medical = DB.Column(DB.Text, nullable=False)
    positive = DB.Column(DB.Text, nullable=False)
    negative = DB.Column(DB.Text, nullable=False)


class Cannabis:
    def __init__(self, Strain, flavors, medical, positive, negative):
        self.Strain=Strain
        self.flavors=flavors
        self.medical=medical
        self.positive=positive
        self.negative=negative
    def strain_features(self):
        print(
        "This strain is " + self.Strain +", "+ self.medical +", "+ self.flavors
        +", "+ self.positive +", "+ self.negative)

sample = Cannabis('indica', 'lemon', 'headache', 'relax', 'tired')
sample.strain_features()
