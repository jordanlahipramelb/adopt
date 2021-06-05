from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Name", validators=[InputRequired(message="Name cannot be blank.")])

    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter a number between 0-30")])

    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")