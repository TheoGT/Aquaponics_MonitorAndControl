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
    lastUpdate = 'today'
    csv = np.genfromtxt('static/csv/temperatures.csv',delimiter = ",")
    return render_template("Temperature(Ambient).html",value = int(csv[-1,0]))

if __name__ == "__main__":
    app.run(debug=True)