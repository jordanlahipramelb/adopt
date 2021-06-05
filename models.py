from flask_sqlalchemy import SQLAlchemy


DEFAULT_PET_PHOTO = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):

        # returns the photo_url in the model or the DEFAULT
        return self.photo_url or DEFAULT_PET_PHOTO

    def __repr__(self):
        """Show info about pet."""

        p = self
        return f"<Pet {p.id}: {p.name}, {p.species}, {p.age}, {p.notes}, {p.available}>"