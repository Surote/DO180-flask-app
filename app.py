from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    req_here=os.getenv("API","API2")
    req=requests.get(req_here)
    if req.status_code != 200:
        print('API 1 not works!!')
        req_here2=os.getenv("API2","API")
        req2=requests.get(req_here2)
        data=json.loads(req2.text)
        return data
    else:
        data=json.loads(req.text)
        return data

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
