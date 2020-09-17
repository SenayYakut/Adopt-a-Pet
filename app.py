from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route("/")
def index():
  return f'''<h1>Adapt a pet</h1>
  <p>Browse through the links below to find your new  furry friend:</p>
  <ul>
    <li><a href = '/animals/dogs'>Dogs</a></li>
    <li><a href = '/animals/cats'>Cats</a></li>
    <li><a href = '/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route("/animals/<pet_type>")
def animals(pet_type):
  html = f"<h1>List of {pet_type}</h1>"
  html += "<ul>"
  for idx, item in enumerate(pets[pet_type]):
    html += "<li>" + f'<a href="/animals/{pet_type}/{idx}">' + item["name"] + "</a></li>"
  html += "</ul>"
  return html


@app.route("/animals/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  name = pet["name"]
  src = pet["url"]
  description = pet["description"]
  breed = pet["breed"]
  age = pet["age"]


  return f'''<h1>{name}</h1>
  <img src={src}>
  <p>{description}</p>
  <ul>
    <li>Breed: {breed}</li>
    <li>Age: {age}</li>
  </ul>
  '''
 
  