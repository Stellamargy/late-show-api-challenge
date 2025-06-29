from server import bcrypt,db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
class Appearance(db.Model):
    
    #table name
    __tablename__ = 'appearances'
    # table columns
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete='CASCADE'), nullable=False)


    #Relationships
    guest = db.relationship('Guest', back_populates='appearances')
    episode=db.relationship('Episode',back_populates='appearances')

    #check constraint to enforce rating range 1-5 at database level
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
    )
    #validates rating column - rating should be an integer 1-5
    @validates('rating')
    def validate_rating(self,key, value):
        if not (1 <= value <= 5):
            raise ValueError('Rating must be between 1 and 5.')
        elif not isinstance(value, int):
            raise ValueError('Rating must be an integer.')
        return value 
