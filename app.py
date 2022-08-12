from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THISISASECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Show list of pets"""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show form to add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    else:
        return render_template("add.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    else:
        """If form fails, redirect back to edit."""
        return render_template("edit.html", pet=pet, form=form)