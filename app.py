from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    req_here=os.getenv(API,"not found")
    req=requests.get(req_here)
    data=json.loads(req.text)
    return data
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
