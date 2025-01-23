import json, os, random
from flask import Flask, request, render_template, redirect, jsonify

app= Flask(__name__) #nome della flask application

#/path della risorsa a cui vogliamo accedere
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    


#GET
#POST
#DELETE
#PUT