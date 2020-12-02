from flask import Flask, render_template      
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route("/")
def home():
    ambientT = np.genfromtxt('static/csv/temperatures.csv',delimiter=",")
    pH = np.genfromtxt('static/csv/pH.csv',delimiter=",")
    return render_template("index.html",ambientTemp = int(ambientT[-1,1]), pH = pH[-1,1])

# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route("/Atemp")
def Atemp():
    csv = np.genfromtxt('static/csv/temperatures.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    
    return render_template("Temperature(Ambient).html",value = int(csv[-1,0]), monthmin = int(csv[10,0]), monthmax = int(csv[-1,0]))

@app.route("/pH")
def pH():
    csv = np.genfromtxt('static/csv/pH.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    
    return render_template("pH.html")

if __name__ == "__main__":
    app.run(debug=True)