import json, os, random
from flask import Flask, request, render_template, redirect

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

if __name__ == "__main__":
     app.run(debug=True)

#app è il nome della flask application

class Animal:
    def __init__(self, AnimalId, AnimalArea, AnimalWeight,AnimalSpecies):
        self.ID = AnimalId
        self.Area = AnimalArea
        self.Weight = AnimalWeight
        self.Species = AnimalSpecies
    
    def getID(self):
        return self.ID
    
    def getArea(self):
        return self.Area
    
    def getWeight(self):
        return self.Weight
    
    def getSpecies(self):
        return self.Species


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
    
#carica i dati degli animali da un file JSON (dati.json), 
#li trasforma in oggetti Animal, e quindi li passa al template agg-togli.html per la visualizzazione:
@app.route("/animals", methods=['GET'])
def get_animals():
    with open('./FileJson/dati.json', 'r') as file: #apriamo il file json
        data = json.load(file)
        
    anList = [] #creaiamo la lista di animali e ci aggiungiamo quello inserito ora
    
    for jsonFile in data:
        animale = Animal(int(jsonFile['ID']), jsonFile['SPECIE'], jsonFile['AREA'], jsonFile['PESO'])
        anList.append(animale)
    
    return render_template('agg-togli.html', dati = anList)

#aggiunge un nuovo animale al file JSON. 
#La logica prevede di ottenere l'ID dell'animale successivo incrementando l'ultimo ID:

@app.route("/new", methods=['POST'])
def add_animale():
    
    with open('./FileJson/dati.json', 'r') as file:
        data = json.load(file)
    
    lastAId = data[-1]['ID']
    
    if lastAId != '':
        lastAId = int(lastAId) + 1
    else:
        lastAId = 1
   
    a_specie = request.form.get('Specie_animale')
    a_area = request.form.get('Area_animale')
    a_peso = request.form.get('Peso_animale')
    newA = Animal(lastAId, a_specie, a_area, a_peso)
        
    data.append(newA.__dict__) #aggiunge il nuovo animale
    
    # modifica json con nuovo animale
    with open('./FileJson/dati.json', 'w') as outfile:
        json.dump(data, outfile)

    return render_template('agg.togli.html')
    
@app.route("/edit", methods=['GET'])
def edit():
    a_id = int(request.args.get('id'))
    
    # Get user info from json file
    with open('./FileJson/dati.json', 'r') as file:
        data = json.load(file)
    
    # Search user
    for i in range(len(data)):
        if int(data[i]['ID']) == a_id:
            json = data[i]
            break
    
    # passo ad html
    AToEdit = Animal(json['ID'], json['SPECIE'], json['AREA'], json['PESO'])
    
    return render_template('edit.html', Animal=AToEdit)
    
#ermette di salvare le modifiche apportate a un animale. L'animale modificato sostituisce l'originale nel file JSON:
@app.route('/save', methods=['POST'])
def modifica():
    # Get parameters from html form
    a_id = int(request.form.get('userId'))
    a_specie = request.form.get('Specie_animale')
    a_area = request.form.get('Area_animale')
    a_peso = request.form.get('Peso_animale')
 
    
    modifiedAnimals = Animal(a_id, a_specie, a_area, a_peso)
    
    # Get user info from json file
    with open('./FileJson/dati.json', 'r') as file:
        data = json.load(file)
    
    # Check user position and remove it from file
    for i in range(len(data)):
        if int(data[i]['ID']) == a_id:
            data.pop(i)
            break
    
    # Add the modified user like new one
    data.append(modifiedAnimals.__dict__)
    
    # Save updated JSON file
    with open('./FileJson/dati.json', 'w') as outfile:
        json.dump(data, outfile)
    
    return redirect('/animals')


@app.route('/delete', methods=['POST'])
def remove_user():
    a_id = int(request.form.get('userId'))
    
    with open('./FileJson/dati.json', 'r') as file:
        data = json.load(file) 
    
    for i in range(len(data)):
        if int(data[i]['ID']) == a_id:
            data.pop(i)
            break
    
    # Save updated JSON file
    with open('./FileJson/dati.json', 'w') as outfile:
        json.dump(data, outfile)
        
    return redirect('/animals')

