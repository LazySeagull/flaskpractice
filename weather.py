from flask import Flask
from configparser import ConfigParser
import requests

config = ConfigParser()
config.read('flaskkipracticekrlo/config.cfg')
api_key = config.get('API','api_key')
api_url = ('http://api.openweathermap.org/data/2.5/weather?zip={},us&mode=json&units=imperial&appid={}')

app = Flask(__name__)

def query_api(zip):
    try:
        data = requests.get(api_url.format(zip , api_key)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

@app.route('/weather/<zip>')
def result(zip):
    resp = query_api(zip)
    try:
        text = resp["name"] + "temperature is " + str(resp["main"]["temp"]) + "degrees Fahrenheit with" + resp["weather"][0]["description"] + "."
    except:
        text = "there was an error the used zip is wrong"
    return text

if __name__ == "__main__":
    app.run(debug = True)



