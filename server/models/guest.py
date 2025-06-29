from server import bcrypt,db
class Guest(db.Model):
    #table name
    __tablename__ = 'guests'
    #columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100),nullable=False)

    # One guest can appear in many appearances
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete', passive_deletes=True)