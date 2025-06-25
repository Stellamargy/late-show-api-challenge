from .database import db
class Episode(db.Model):
    #table names
    _tablename__ = 'episodes'
    #columns and their respective constraints
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # One episode can have many appearances
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete', passive_deletes=True)
    
