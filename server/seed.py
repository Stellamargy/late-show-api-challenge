# Seed Database- Get testing data 
from server.models import User,Guest,Episode,Appearance
from .extensions import db,fake
from .app import app
from random import randint, choice
from datetime import datetime, timedelta


def seed_data():
    with app.app_context():
        #Reset db - seed data only once
        db.drop_all()
        db.create_all()

        #user dummy data
        users=[]
        for _ in range(5):
            user=User(username=fake.user_name())
            user.password="12345"
            users.append(user)
        db.session.add_all(users)

        # Guests  dummy data 
        guests = []
        for _ in range(10):
            guest = Guest(name=fake.name(), occupation=fake.job())
            guests.append(guest)
        db.session.add_all(guests)


        # Episodes Dummy data
        episodes = []
        for i in range(1, 11):
            episode = Episode(date=datetime.now().date() - timedelta(days=i), number=i)
            episodes.append(episode)
        db.session.add_all(episodes)

        db.session.flush()

       
        appearances = []
        for _ in range(20):
            appearance = Appearance(
                rating=randint(1, 5),
                guest=choice(guests),
                episode=choice(episodes)
            )
            appearances.append(appearance)
        db.session.add_all(appearances)

        db.session.commit()

        print("Seeding Complete")


# call seed method to populate data
seed_data()



