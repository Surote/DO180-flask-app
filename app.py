from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        req_here=os.getenv("API","API2")
        req=requests.get(req_here)
        data=json.loads(req.text)
        return data
    except:
        req_here=os.getenv("API2","API")
        req=requests.get(req_here)
        data=json.loads(req.text)
        return data

    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234)
