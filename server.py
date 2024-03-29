from flask import Flask, send_from_directory, jsonify, render_template
from flask_caching import Cache

from settings import roomOutlookIds, locations

import requests

from datetime import datetime, timedelta

def getStartDateLabel():
    # return "2023-02-01"
    return datetime.now().strftime("%Y-%m-%d")

def getEndDateLabel():
    # return "2023-02-02"
    return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

# Setup cache
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/node_modules/<path:path>')
def send_js(path):
    return send_from_directory('node_modules', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('img', 'favicon.ico')

@app.route('/')
def root():
    theLocations = { id:data['title'] for id,data in locations.items() }
    return render_template('index.html', locations=theLocations)

@app.route('/location/<location>')
def location(location):
    rooms = locations[location]['rooms']
    mapImg = locations[location]['map']
    targetDate = getStartDateLabel()
    return render_template('location.html', targetDate=targetDate, rooms=rooms,
                            mapImg = mapImg)

@app.route('/api/calendar/<calName>')
@cache.cached(timeout=60)
def calendar(calName):
    # Generate these automatically
    startDate = getStartDateLabel()
    endDate   = getEndDateLabel()
    outlookId = roomOutlookIds[calName]
    url = 'https://outlook.office365.com/owa/calendar/%s/service.svc?action=FindItem&ID=-1&AC=1'%outlookId

    bodyTemplate = open('bodyTemplate.txt', 'r').read()
    body = bodyTemplate%(startDate, endDate)
    headers = { 'Action': 'FindItem', "Content-Type": "application/json; charset=UTF-8" }

    calData = []
    try:
        resp = requests.post(url, headers=headers, data=body)
        respJson = resp.json()

        # Name the things in between just for fun ?
        events = respJson['Body']['ResponseMessages']['Items'][0]['RootFolder']['Items']

        for event in events:
            calEvent = {
                'resourceId': calName,
                'id'        : event['ItemId']['Id'],
                'start'     : event['Start'],
                'end'       : event['End'],
                'title'     : event['Subject']
            }
            calData.append(calEvent)
        status = 'ok'
    except Exception as e:
        status = 'error -- ' + str(e)
    return jsonify(data=calData, status=status)


if __name__ == "__main__":
    app.run(debug=True)
