from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    req=requests.get('http://worldclockapi.com/api/json/est/now')
    data=json.loads(req.text)
    return data
if __name__ == '__main__':
    app.run()
