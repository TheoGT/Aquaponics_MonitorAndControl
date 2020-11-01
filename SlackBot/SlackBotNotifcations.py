import jupyter_slack
import os
import csv

# System Monitoring Bot https://api.slack.com/apps/A01CT0FBC77/general?

# Slack notifications using jupyter_slack package https://github.com/keitakurita/jupyter-slack-notify
os.environ['SLACK_WEBHOOK_URL'] = ''

# Current values for environmental variables
#   CHECK TO MAKE SURE INCOMING UNITS MATCH UNITS OF RANGES

# μS/cm, L/min, L/min, %, mg/L, pH, F, F, cm
allCurVal = {"EC": 0, "flowRateNFT":3, "flowRateDWC":2, "humidity":80, "nitrate":15, "pH":7, "temperatureAmbient":71, "temperatureWater":60, "waterLevel":8}
formattedName = {"EC": "Electrical Conductivity", "flowRateNFT": "Flow Rate for NFT", "flowRateDWC":"Flow Rate for DWC", "humidity": "Humidity", "nitrate":"Nitrate", "pH":"pH", "temperatureAmbient": "Ambient Temperature", "temperatureWater": "Water Temperature", "waterLevel": "Water Level"}

# Importing List of min and max ideal ranges for each environmental variable and the units
# The percent above the min and max values that will send a warning notifcation
warningPercent = 0.1

header = None

with open('Acceptable Ranges for Sensors.csv', 'rt') as f:
    csv_reader = csv.reader(f)

    for line in csv_reader:
        if header == None: header = line
        
        else:
            var = line[0]
            minVal = float(line[1])
            maxVal = float(line[2])
            units = line[3]
            curVal = allCurVal[var]
            warningAmount = (maxVal - minVal) * warningPercent

            if minVal <= curVal <= maxVal:

                # Checks if curVal is within the green range
                if minVal + warningAmount <= curVal <= maxVal - warningAmount:
                    # print("minVal:", minVal)
                    # print("warningAmount:", warningAmount)
                    # print("curVal:", curVal)
                    # print("maxVal:", maxVal)
                    pass

                # curVal is in the warning range
                else:
                    jupyter_slack.notify_self(":warning: WARNING :warning: \n" + formattedName[var] + " is " + str(curVal) + " " + units + "\nAcceptable range is " + str(minVal) + " - " + str(maxVal) + " " + units)
                    pass

            # curVal is outside the range and sends alert
            else:
                jupyter_slack.notify_self(":rotating_light: ALERT :rotating_light: \n" + formattedName[var] + " is " + str(curVal) + " " + units + "\nAcceptable range is " + str(minVal) + " - " + str(maxVal) + " " + units)
                pass




