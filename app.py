from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    req_here=os.getenv("API","API2")
    req=requests.get("http://"+req_here)
    
    if req.status_code != 200:
        req_here=os.getenv("API2","API")
        req=requests.get("http://"+req_here)
    
    if req.status_code != 200:
        return 'no API found'
    data=json.loads(req.text)
    return data
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
