from flask import Flask, render_template      
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route("/temp")
def temp():
    csvFileName = 'CommDemo/MultipleSensorsTest/ping1.csv'
    csv = np.genfromtxt(csvFileName,delimiter = ",")
    #lastvalue = csv[-1,0]
    #monthmax = lastval % 10000
    #, monthmin = int(csv[10,0]), monthmax = int(csv[-1,0])
    return render_template("Temperature(Ambient).html",value = int(csv[-1,1]), csvFile = "../" + csvFileName)
    #return render_template("temp.html")

if __name__ == "__main__":
    app.run(debug=True)