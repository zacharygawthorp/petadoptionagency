from optparse import OptionConflictError
from tkinter import PhotoImage
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Edit an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")