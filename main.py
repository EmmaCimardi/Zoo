import json, os
from flask import Flask, request, render_template, redirect 

class Animal:
    def __init__(self, AnimalId, AnimalName, AnimalWeight,AnimalSpecies ):
        self.ID = AnimalId
        self.FirstName = AnimalName
        self.Weight = AnimalWeight
        self.Species = AnimalSpecies
    
    def getID(self):
        return self.ID
    
    def getFirstName(self):
        return self.FirstName
    
    def getWeight(self):
        return self.Weight
    
    def getSpecies(self):
        return self.Species
    
    # Root / path for index page
@app.route('/', methods=['GET'])
def index():
    devName = 'Luca Roveroni'
    return render_template('index.html', dev_name=devName)

# Get Animals from file
# Path: GET /Animals
@app.route('/Animals', methods=['GET'])
def get_Animals():
    with open('./db/Animals.json', 'r') as file:
        data = json.load(file)
        
    AnimalList = []
    
    # Cycle over each JSON object and create a new Animal object
    for jsonFile in data:
        Animal = Animal(int(jsonFile['ID']), jsonFile['FirstName'], jsonFile['Weight'], jsonFile['Species'])
        AnimalList.append(Animal)
    
    return render_template('index.html', Animal=AnimalList)

# Add Animal to file
# Path: POST /new
@app.route('/new', methods=['POST'])
def add_Animal():
    # Open Animal file
    with open('./db/Animals.json', 'r') as file:
        data = json.load(file)
    
    # Check last used id and increment it
    lastAnimalId = data[-1]['ID']
    if lastAnimalId != '':
        lastAnimalId = int(lastAnimalId) + 1
    else:
        lastAnimalId = 1
    
    
        
    # Add new Animal to Animals
    data.append(newAnimal.__dict__)
    
    # Save updated JSON file
    with open('./db/Animals.json', 'w') as outfile:
        json.dump(data, outfile)
    
    return redirect('/Animals')

# Render EDIT page
# Path: GET /edit?id=XX
@app.route('/edit', methods=['GET'])
def show_edit_Animal():
    Animal_id = int(request.args.get('id'))
    
    # Get Animal info from json file
    with open('./db/Animals.json', 'r') as file:
        data = json.load(file)
    
    # Search Animal
    for i in range(len(data)):
        if int(data[i]['ID']) == Animal_id:
            jsonAnimal = data[i]
            break
    
    # Pass Animal object to html template 
    AnimalToEdit = Animal(jsonAnimal['ID'], jsonAnimal['FirstName'], jsonAnimal['Weight'], jsonAnimal['Birthday'], jsonAnimal['Species'])
    
    return render_template('edit.html', Animal=AnimalToEdit)

# Save modified existing Animal in file
# Path: POST /save
@app.route('/save', methods=['POST'])
def edit_Animal():
    # Get parameters from html form
    Animal_id = int(request.form.get('AnimalId'))
    Animal_first_name = request.form.get('AnimalFirstName')
    Animal_last_name = request.form.get('AnimalWeight')
    Animal_birthday = request.form.get('AnimalBirthday')
    Animal_Species = request.form.get('')
    
    modifiedAnimal = Animal(Animal_id, Animal_first_name, Animal_last_name, Animal_birthday, Animal_Species)
    
    # Get Animal info from json file
    with open('./db/Animals.json', 'r') as file:
        data = json.load(file)
    
    # Check Animal position and remove it from file
    for i in range(len(data)):
        if int(data[i]['ID']) == Animal_id:
            data.pop(i)
            break
    
    # Add the modified Animal like new one
    data.append(modifiedAnimal.__dict__)
    
    # Save updated JSON file
    with open('./db/Animals.json', 'w') as outfile:
        json.dump(data, outfile)
    
    return redirect('/Animals')

# Remove Animal in file
# Path: POST /delete
@app.route('/delete', methods=['POST'])
def remove_Animal():
    Animal_id = int(request.form.get('AnimalId'))
    
    # Open JSON file
    with open('./db/Animals.json', 'r') as file:
        data = json.load(file) 
    
    # Remove the Animal from JSON file
    for i in range(len(data)):
        if int(data[i]['ID']) == Animal_id:
            data.pop(i)
            break
    
    # Save updated JSON file
    with open('./db/Animals.json', 'w') as outfile:
        json.dump(data, outfile)
        
    return redirect('/Animals')