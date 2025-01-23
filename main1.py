import json, os, random
from flask import Flask, request, render_template, redirect, jsonify

app= Flask(__name__) #nome della flask application

@app.route("/") #/path della risorsa a cui vogliamo accedere
def home():
    return "Home";

if __name__ == "__main__":
    app.run(debug=True)
    
#GET
#POST
#DELETE
#PUT