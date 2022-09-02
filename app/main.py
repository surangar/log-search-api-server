from flask import Flask
from flask import json
from datetime import date
from flask import Flask, render_template, request
import sys

app = Flask(__name__)


def log_read(key): # This function Search given date in the logs
    infile = r"/var/log/search-api/index.html"
    important = []
    keep_phrases = []
    keep_phrases.append(key)
    with open(infile) as f:
        f = f.readlines()
    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important

@app.route('/getlogs', methods=['GET', 'POST']) # This route to get logs of perticular key search
def get_logs():
    log = []
    key_search = request.form['key']
    if(len(key_search)):
        log = log_read(key_search)
        json_string = json.dumps(log)
    else:
        log = ['empty_search_key']
        json_string = json.dumps(log) 
    
    return json_string

@app.route('/', methods=['GET', 'POST']) # This route to get the help
def home():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)