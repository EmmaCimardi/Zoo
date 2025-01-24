import json, os, random
from flask import Flask, request, render_template, redirect

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

#app è il nome della flask application

class Animal:
    def __init__(self, AnimalId, AnimalArea, AnimalWeight,AnimalSpecies):
        self.ID = AnimalId
        self.Area = AnimalArea
        self.Weight = AnimalWeight
        self.Species = AnimalSpecies
    
    def getID(self):
        return self.ID
    
    def getFirstArea(self):
        return self.FirstArea
    
    def getWeight(self):
        return self.Weight
    
    def getSpecies(self):
        return self.Species


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route("/animals", methods=['GET'])
def get_animals():
    with open('./FileJson/dati.json', 'r') as file: #apriamo il file json
        data = json.load(file)
        
    anList = [] #creaiamo la lista di animali e ci aggiungiamo quello inserito ora
    
    # Cycle over each JSON object and create a new User object
    for jsonFile in data:
        animale = Animal(int(jsonFile['ID']), jsonFile['SPECIE'], jsonFile['AREA'], jsonFile['PESO'])
        anList.append(animale)
    
    return render_template('agg-togli.html', animali = anList)


if __name__ == "__main__":
    app.run(debug=True)
#GET
#POST
#DELETE
#PUT