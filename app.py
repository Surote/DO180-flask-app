from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    req=requests.get('https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Bangkok')
    data=json.loads(req.text)
    return data
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
