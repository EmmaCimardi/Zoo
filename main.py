import json, os, random
from flask import Flask, request, render_template, redirect 

class Client:
    def __init__(self, ClientId, ClientName, ClientLastName,  ClientNationality):
        self.ID = ClientId
        self.FirstName = ClientName
        self.LastName = ClientLastName
        self.Nationality = ClientNationality
    
    def getID(self):
        return self.ID
    
    def getFirstName(self):
        return self.FirstName
    
    def getLastName(self):
        return self.LastName
    
    def getNationality(self):
        return self.Nationality
    
    # Root / path for index page
@app.route('/', methods=['GET'])
def index():
    devName = 'Luca Roveroni'
    return render_template('index.html', dev_name=devName)

# Get Clients from file
# Path: GET /Clients
@app.route('/Clients', methods=['GET'])
def get_Clients():
    with open('./db/Clients.json', 'r') as file:
        data = json.load(file)
        
    ClientList = []
    
    # Cycle over each JSON object and create a new Client object
    for jsonFile in data:
        Client = Client(int(jsonFile['ID']), jsonFile['FirstName'], jsonFile['LastName'], jsonFile['Nationality'])
        ClientList.append(Client)
    
    return render_template('index.html', client=ClientList)

# Add Client to file
# Path: POST /new
@app.route('/new', methods=['POST'])
def add_Client():
    # Open Client file
    with open('./db/Clients.json', 'r') as file:
        data = json.load(file)
    
    # Check last used id and increment it
    lastClientId = data[-1]['ID']
    if lastClientId != '':
        lastClientId = int(lastClientId) + 1
    else:
        lastClientId = 1
    
    
        
    # Add new Client to Clients
    data.append(newClient.__dict__)
    
    # Save updated JSON file
    with open('./db/Clients.json', 'w') as outfile:
        json.dump(data, outfile)
    
    return redirect('/Clients')

# Render EDIT page
# Path: GET /edit?id=XX
@app.route('/edit', methods=['GET'])
def show_edit_Client():
    Client_id = int(request.args.get('id'))
    
    # Get Client info from json file
    with open('./db/Clients.json', 'r') as file:
        data = json.load(file)
    
    # Search Client
    for i in range(len(data)):
        if int(data[i]['ID']) == Client_id:
            jsonClient = data[i]
            break
    
    # Pass Client object to html template 
    ClientToEdit = Client(jsonClient['ID'], jsonClient['FirstName'], jsonClient['LastName'], jsonClient['Birthday'], jsonClient['Nationality'])
    
    return render_template('edit.html', Client=ClientToEdit)

# Save modified existing Client in file
# Path: POST /save
@app.route('/save', methods=['POST'])
def edit_Client():
    # Get parameters from html form
    Client_id = int(request.form.get('ClientId'))
    Client_first_name = request.form.get('ClientFirstName')
    Client_last_name = request.form.get('ClientLastName')
    Client_birthday = request.form.get('ClientBirthday')
    Client_nationality = request.form.get('ClientNationality')
    
    modifiedClient = Client(Client_id, Client_first_name, Client_last_name, Client_birthday, Client_nationality)
    
    # Get Client info from json file
    with open('./db/Clients.json', 'r') as file:
        data = json.load(file)
    
    # Check Client position and remove it from file
    for i in range(len(data)):
        if int(data[i]['ID']) == Client_id:
            data.pop(i)
            break
    
    # Add the modified Client like new one
    data.append(modifiedClient.__dict__)
    
    # Save updated JSON file
    with open('./db/Clients.json', 'w') as outfile:
        json.dump(data, outfile)
    
    return redirect('/Clients')

# Remove Client in file
# Path: POST /delete
@app.route('/delete', methods=['POST'])
def remove_Client():
    Client_id = int(request.form.get('ClientId'))
    
    # Open JSON file
    with open('./db/Clients.json', 'r') as file:
        data = json.load(file) 
    
    # Remove the Client from JSON file
    for i in range(len(data)):
        if int(data[i]['ID']) == Client_id:
            data.pop(i)
            break
    
    # Save updated JSON file
    with open('./db/Clients.json', 'w') as outfile:
        json.dump(data, outfile)
        
    return redirect('/Clients')