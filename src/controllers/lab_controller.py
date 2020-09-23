from src.app import app
from src.database import db
from flask import request
from bson.json_util import dumps
from src.controllers.functions import *
from ..helpers.json_response_labs import asJsonResponseLabs
import random



@app.route("/lab/create/<name>")
def create_lab(name):
    new_lab = {
    'Lab': name}
    result = db.pull_request.insert_one(new_lab)
    return {'_id': str(result.inserted_id)}

'''
@app.route("/lab/search/<name>")
@asJsonResponseLabs
def search_lab(name):
    query = {'Lab':name}
    result = db.pull_request.find(query)
    res = 
    return result
'''

@app.route("/lab/<lab_prefix>/search")
def searchLab(lab_prefix):   
    opened_pr = db.pull_request.find({"$and":[{"Lab":lab_prefix},{"State": "open"}]}).count()
    closed_pr = db.pull_request.find({"$and":[{"Lab":lab_prefix},{"State": "closed"}]}).count()
    percent = f'{str(int(closed_pr/(opened_pr+closed_pr)*100))}%'

    
    result={'· El numero de PR abiertas es': opened_pr,
    '· El numero de PR cerradas es': closed_pr,
    '· El porcentaje de PR cerradas es':percent
    
    }
  
    return dumps(result)



@app.route("/lab/memeranking")
def meme_ranking():
    pass

'''
@app.route("/lab/<lab>/meme")
def random_meme(lab):
    result=db.pull_request.aggregate([  
        { "$sample": {"size": 1} }, 
        { "$match":  {"Lab": lab} },
        { "$project": { "Url" : 1, "_id": 0}}
      ])
    return dumps(result)
'''
'''
@app.route("/lab/<lab>/meme")
def random_meme(lab):
    result = random.choice(db.pull_request.find({"Lab":lab},{'Url':1}))
    return result
'''