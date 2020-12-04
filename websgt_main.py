from flask import Flask, render_template      
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route("/")
def home():
    ambientT = np.genfromtxt('static/csv/temperatures.csv',delimiter=",")
    pH = np.genfromtxt('static/csv/pH.csv',delimiter=",")
    humidity = np.genfromtxt('static/csv/humidity.csv',delimiter=",")
    return render_template("index.html",ambientTemp = int(ambientT[-1,1]), pH = pH[-1,1], humidity = humidity[-1,1])

# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route("/Atemp")
def Atemp():
    csv = np.genfromtxt('static/csv/temperatures.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    #, monthmin = int(csv[10,0]), monthmax = int(csv[-1,0])
    return render_template("Temperature(Ambient).html",value = int(csv[-1,1]), csvFile = "../" + csvFileName)
    #return render_template("temp.html")

@app.route("/pH")
def pH():
    csv = np.genfromtxt('static/csv/pH.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    
    return render_template("pH.html")

@app.route("/humidity")
def humidity():
    csv = np.genfromtxt('static/csv/humidity.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    
    return render_template("humidity.html")

if __name__ == "__main__":
    app.run(debug=True)