from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li>
      <a href="/animals/dogs">Dogs</a>
    </li>
    <li>
    <a href="/animals/cats">Cats</a>
    </li>
    <li>
      <a href="/animals/rabbits">Rabbits</a>
    </li>
  </ul>
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type}</h1>"
  html += "<ul>"
  for pet in pets[pet_type]:
    element = pet.get('name', 'ERROR')
    html += f"<li>{element}</li>"
  html += "</ul>"
  return html


@app.route('/animals/<string:pet_type>')
def animals_list(pet_type):
  html = f"<h1>List of {pet_type}"
  return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  print(pet)
  pet_id += 1
  html = f"<h1>This is {pet_type} number {pet_id}"
  element = pet.get('name', 'ERROR')
  html += f'<h1>Name: {element}</h1>'
  element = pet.get('age', 'ERROR')
  html += f'<h2>Age: {element}</h2>'
  element = pet.get('breed', 'ERROR')
  html += f'<h3>Breed: {element}</h3>'
  element = pet.get('description', 'ERROR')
  html += f'<p>Description: {element}</p>'
  element = pet.get('url', 'ERROR')
  html += f'<img src="{element}"></img>'
  return html


@app.route('/dogs')
def dogs():
  return '''The dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct gray wolves,[6][7] and the gray wolf is the dog's closest living relative.[8] The dog was the first species to be domesticated[9][8] by humans. Hunter-gatherers did this over 15,000 years ago in Oberkassel, Bonn,[7] which was before the development of agriculture.[1] Due to their long association with humans, dogs have expanded to a large number of domestic individuals[10] and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[11]

The dog has been selectively bred over millennia for various behaviors, sensory capabilities, and physical attributes.[12] Dog breeds vary widely in shape, size, and color. They perform many roles for humans, such as hunting, herding, pulling loads, protection, assisting police and the military, companionship, therapy, and aiding disabled people. Over the millennia, dogs became uniquely adapted to human behavior, and the human–canine bond has been a topic of frequent study.[13] This influence on human society has given them the sobriquet of "man's best friend".'''


@app.route('/cats')
def cats():
  return '''
  The cat (Felis catus), commonly referred to as the domestic cat or house cat, is the only domesticated species in the family Felidae. Recent advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly kept as a house pet and farm cat, but also ranges freely as a feral cat avoiding human contact. It is valued by humans for companionship and its ability to kill vermin. Because of its retractable claws, it is adapted to killing small prey like mice and rats. It has a strong, flexible body, quick reflexes, sharp teeth, and its night vision and sense of smell are well developed. It is a social species, but a solitary hunter and a crepuscular predator. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling, and grunting as well as cat body language. It can hear sounds too faint or too high in frequency for human ears, such as those made by small mammals. It also secretes and perceives pheromones.

Female domestic cats can have kittens from spring to late autumn in temperate zones and throughout the year in equatorial regions, with litter sizes often ranging from two to five kittens. Domestic cats are bred and shown at events as registered pedigreed cats, a hobby known as cat fancy. Animal population control of cats may be achieved by spaying and neutering, but their proliferation and the abandonment of pets has resulted in large numbers of feral cats worldwide, contributing to the extinction of bird, mammal and reptile species.
  '''


@app.route('/rabbits')
def rabbits():
  return '''Rabbits, also known as bunnies or bunny rabbits, are small mammals in the family Leporidae (which also includes the hares), which is in the order Lagomorpha (which also includes the pikas). Oryctolagus cuniculus is the European rabbit, including its descendants, the world's 305 breeds[1] of domestic rabbit. Sylvilagus includes 13 wild rabbit species, among them the seven types of cottontail. The European rabbit, which has been introduced on every continent except Antarctica, is familiar throughout the world as a wild prey animal, a domesticated form of livestock and a pet. With its widespread effect on ecologies and cultures, in many areas of the world, the rabbit is a part of daily life – as food, clothing, a companion, and a source of artistic inspiration.

Although once considered rodents, lagomorphs like rabbits have been discovered to have diverged separately and earlier than their rodent cousins and have a number of traits rodents lack, including two extra incisors.'''


app.run(debug=True, host="0.0.0.0")
