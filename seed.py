"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# # Make a bunch of pets

astro = Pet(name="Astro", species="dog", age="2", available=False)
lucy = Pet(name="Lucy", species="dog", age="4")
stella = Pet(name="Stella", species="dog", age="1")
kimbo = Pet(name="Kimbo", species="dog", age="4")
rocket = Pet(name="Rocket", species="porcupine", age="2")
sam = Pet(name="Sam", species="dog", age="5")
bogey = Pet(name="Bogey", species="dog", age="1")


db.session.add_all([astro, lucy, stella, kimbo, rocket, sam, bogey])
db.session.commit()
