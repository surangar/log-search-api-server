from flask import Flask
from flask import json
from datetime import datetime
from flask import Flask, render_template, request
import sys

app = Flask(__name__)


def log_read(date): # This function Search given date in the logs
    infile = r"/var/log/search-api/index.html"
    important = []
    keep_phrases = []
    keep_phrases.append(date)
    with open(infile) as f:
        f = f.readlines()
    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important

@app.route('/getlogs', methods=['GET', 'POST'])
def get_logs():
    date_search = request.form['date']
    log = []
    log = log_read(date_search)

    json_string = json.dumps(log)
    return json_string

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)