from flask import Flask, request, send_from_directory, jsonify
from settings import roomOutlookIds

import requests
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/node_modules/<path:path>')
def send_js(path):
    return send_from_directory('node_modules', path)

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/api/calendar/<calName>')
def calendar(calName):
    # Generate these automatically
    startDate = '2017-03-07'
    endDate   = '2017-03-08'
    outlookId = roomOutlookIds[calName]
    url = 'https://outlook.office365.com/owa/calendar/%s/service.svc?action=FindItem&ID=-1&AC=1'%outlookId

    bodyTemplate = open('bodyTemplate.txt', 'r').read()
    body = bodyTemplate%(startDate, endDate)
    headers = { 'Action': 'FindItem', "Content-Type": "application/json; charset=UTF-8" }

    resp = requests.post(url, headers=headers, data=body)
    respJson = resp.json()

    # Name the things in between just for fun ?
    events = respJson['Body']['ResponseMessages']['Items'][0]['RootFolder']['Items']

    calData = []
    for event in events:
        calEvent = {
            'resourceId': calName,
            'id'        : event['ItemId']['Id'],
            'start'     : event['Start'],
            'end'       : event['End'],
            'title'     : event['Subject']
        }
        calData.append(calEvent)

    return jsonify(calData)


if __name__ == "__main__":
    app.run(debug=True)
