import jupyter_slack
import os

# System Monitoring Bot https://api.slack.com/apps/A01CT0FBC77/general?

# Slack notifications using jupyter_slack package https://github.com/keitakurita/jupyter-slack-notify
os.environ['SLACK_WEBHOOK_URL'] = ''

# Current values for environmental variables

EC = [0,2] #
flowRate = [[],[]] # ???
humidity = [30,50] # %
nitrate = [10,20] # mg/ L
pH = [7,9]
temperatureAmbient = [70,85] # Fahrenheight
temperatureWater = [60,75] # Fahrenheight


# Importing List of min and max ideal ranges for each environmental variable and the units

EC = [0,2] #
flowRate = [[],[]] # ???
humidity = [30,50] # %
nitrate = [10,20] # mg/ L
pH = [7,9]
temperatureAmbient = [70,85] # Fahrenheight
temperatureWater = [60,75] # Fahrenheight

if 
    jupyter_slack.notify_self("hello world")



