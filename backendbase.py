import os
import pymongo
import json
import random

def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    rj = request.get_json()
    mongostr = os.environ.get('MONGOSTR')
    client = pymongo.MongoClient(mongostr)
    db = client["covidgame"]
    col = db.gamestate
    results = []
    maxid = 0
    for x in col.find():
        id = x["id"]
        maxid +=1
    fid = str(maxid+1)
    payload = {}
    if rj:

        level = rj['opponents']['COVID-19'][0]['level']
        attack = rj['opponents']['COVID-19'][1]['attack']
        maxhealth = rj['opponents']['COVID-19'][2]['maxhealth']
        remaininghealth = rj['opponents']['COVID-19'][3]['remaininghealth']

        col.update_one({"id": "0"}, {"$set":{"level":level}})
        col.update_one({"id": "0"}, {"$set":{"attack":attack}})
        col.update_one({"id": "0"}, {"$set":{"maxhealth":maxhealth}})
        col.update_one({"id": "0"}, {"$set":{"remaininghealth":remaininghealth}})



        level = rj['opponents']['Player'][0]['level']
        attack = rj['opponents']['Player'][1]['attack']
        maxhealth = rj['opponents']['Player'][2]['maxhealth']
        remaininghealth = rj['opponents']['Player'][3]['remaininghealth']
        strength = rj['opponents']['Player'][4]['strength']
        defense = rj['opponents']['Player'][5]['defense']
        healing = rj['opponents']['Player'][6]['healing']
        luck = rj['opponents']['Player'][7]['luck']
        loot = rj['opponents']['Player'][8]['loot']
        exp = rj['opponents']['Player'][9]['exp']
        

        col.update_one({"id": "1"}, {"$set":{"level":level}})
        col.update_one({"id": "1"}, {"$set":{"attack":attack}})
        col.update_one({"id": "1"}, {"$set":{"maxhealth":maxhealth}})
        col.update_one({"id": "1"}, {"$set":{"remaininghealth":remaininghealth}})

        col.update_one({"id": "1"}, {"$set":{"strength":strength}})
        col.update_one({"id": "1"}, {"$set":{"defense":defense}})
        col.update_one({"id": "1"}, {"$set":{"healing":healing}})
        col.update_one({"id": "1"}, {"$set":{"luck":luck}})
        col.update_one({"id": "1"}, {"$set":{"loot":loot}})
        col.update_one({"id": "1"}, {"$set":{"exp":exp}})
        
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        # retjson['id'] = id

        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
