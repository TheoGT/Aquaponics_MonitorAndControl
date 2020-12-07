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


def getVariables(array, min, max):
    danger = "progress-bar border-danger"
    warning = "progress-bar border-warning"
    safe = "progress-bar border-success"
    mostRecent = array[-1,1]
    if (mostRecent < min or mostRecent > max): color = danger
    elif (mostRecent < min*1.1 or mostRecent > max*.9): color = warning
    else: color = safe
    if (np.size(array,axis = 0) > 12): lastHour = array[-13,1]
    else: lastHour = -1
    if (np.size(array,axis = 0) > 288): lastDay = array[-288,1]
    else: lastDay = -1
    return(color,lastHour,lastDay)

@app.route("/")
def home():
    ambientT = np.genfromtxt('static/csv/temperatures.csv',delimiter=",")
    aTval = ambientT[-1,1]
    (aTcolor,aTlastHour,aTlastDay) = getVariables(ambientT,65,90)

    pH = np.genfromtxt('static/csv/pH.csv',delimiter=",")
    pHval = pH[-1,1]
    (pHcolor,pHlastHour,pHlastDay) = getVariables(pH,6,9)

    humidity = np.genfromtxt('static/csv/humidity.csv',delimiter=",")
    (humidityColor,humidityLastHour,humidityLastDay) = getVariables(humidity,70,90)

    EC = np.genfromtxt('static/csv/EC.csv',delimiter=",")
    (ecColor,ecLastHour,ecLastDay) = getVariables(EC,.5,2)

    return render_template("index.html",ambientTemp = aTval, pH = pHval, humidity = humidity[-1,1], EC = EC[-1,1],
    pHcolor = pHcolor, aTcolor = aTcolor, pHlastHour = pHlastHour, pHlastDay = pHlastDay, aTlastday = aTlastDay, aTlasthour = aTlastHour,
    humidityColor = humidityColor,humidityLastHour = humidityLastHour,humidityLastDay = humidityLastDay,
    ecColor= ecColor,ecLastHour = ecLastHour,ecLastDay = ecLastDay)


@app.route("/Atemp")
def Atemp():
    csv = np.genfromtxt('static/csv/temperatures.csv',delimiter = ",")
    return render_template("Temperature(Ambient).html",value = int(csv[-1,1]))

@app.route("/pH")
def pH():
    csv = np.genfromtxt('static/csv/pH.csv',delimiter = ",")
    return render_template("pH.html")

@app.route("/humidity")
def humidity():
    csv = np.genfromtxt('static/csv/humidity.csv',delimiter = ",")
    return render_template("humidity.html")

@app.route("/EC")
def EC():
    csv = np.genfromtxt('static/csv/EC.csv',delimiter = ",")
    return render_template("EC.html")

@app.route("/slack")
def slack():
    return render_template("slack.html")

@app.route("/contacts")
def contacts():
    return render_template("ContactInfo.html")

if __name__ == "__main__":
    app.run(debug=True)