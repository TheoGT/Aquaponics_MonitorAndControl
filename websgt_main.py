from flask import Flask, render_template      
import pandas as pd
import numpy as np

app = Flask(__name__)

def getlastweek(csv):
    current = csv[-1,0]
    #looking for day seven days ago, will not work for may 1-6
    day = int(current.split("/")[2]) - 7
    if (day < 1):
        day += 30
    
    #change range depending on frequency of checks (should be around 1.5* expected checks per wee




@app.route("/")
def home():
    ambientT = np.genfromtxt('static/csv/temperatures.csv',delimiter=",")
    pH = np.genfromtxt('static/csv/pH.csv',delimiter=",")
    humidity = np.genfromtxt('static/csv/humidity.csv',delimiter=",")
    EC = np.genfromtxt('static/csv/EC.csv',delimiter=",")
    return render_template("index.html",ambientTemp = int(ambientT[-1,1]), pH = pH[-1,1], humidity = humidity[-1,1], EC = EC[-1,1])

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

@app.route("/EC")
def EC():
    csv = np.genfromtxt('static/csv/EC.csv',delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    return render_template("EC.html")

@app.route("/slack")
def slack():
    return render_template("slack.html")

@app.route("/contacts")
def contacts():
    return render_template("ContactInfo.html")

if __name__ == "__main__":
    app.run(debug=True)