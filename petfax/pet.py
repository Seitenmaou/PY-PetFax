from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>/')
def petDetail(pet_id):
    return  render_template('details.html', pet=pets[pet_id])

@bp.route('/new/')
def newFact():
    return  render_template('new.html')