from flask import ( Blueprint, render_template )
import json 

pets = json.load(open('pets.json'))



bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

# Route for showing details of a specific pet
@bp.route('/<int:pet_id>')
def show(pet_id):

    if 1 <= pet_id <= len(pets):
        pet = pets[pet_id - 1] 
        return render_template('pets/show_pet.html', pet=pet)  
    else:

        return render_template('404.html'), 404