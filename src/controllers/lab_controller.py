from src.app import app
from src.database import db
from flask import request
from bson.json_util import dumps
from src.controllers.functions import *
from ..helpers.json_response_labs import asJsonResponseLabs
from datetime import datetime
import numpy as np



'''
Purpose: Create a lab to be analyzed.
Params: The lab-prefix to be analyzed. Example: [lab-scavengers]
Returns: lab_id
'''
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


'''
Purpose: Search student submissions on specific lab
Params: user_id
Returns: See Lab analysis section
'''
@app.route("/lab/<lab_prefix>/search")
def searchLab(lab_prefix):
    # Number of open PR 
    opened_pr = db.pull_request.find({"$and":[{"Lab":lab_prefix},{"State": "open"}]}).count()
    
    # Number of closed PR
    closed_pr = db.pull_request.find({"$and":[{"Lab":lab_prefix},{"State": "closed"}]}).count()
    
    # Percentage of completeness (closed vs open)
    percent = f'{str(int(closed_pr/(opened_pr+closed_pr)*100))}%'

    # List number of missing PR from students
    missing = db.pull_request.find({"Lab":lab_prefix},{'User':1,'User2':1})

    
    # Instructor grade time in hours: (max, min and mean)
    grade_time = db.pull_request.find({"Lab":lab_prefix},{'Open':1,'Closed':1})  
    grade_time_list=[]
    for i in grade_time:
        op = datetime.fromisoformat(i['Open'].replace('Z',''))
        cl = datetime.fromisoformat(i['Closed'].replace('Z',''))
        grade_time_list.append((cl-op).total_seconds())

    result={'· El numero de PR abiertas es': opened_pr,
    '· El numero de PR cerradas es': closed_pr,
    '· El porcentaje de PR cerradas es':percent,
    f'· El tiempo máximo de corrección del lab {lab_prefix} es': (f'{str(round(max(grade_time_list)/3600,2))}h'),
    f'· El tiempo mínimo de corrección del lab {lab_prefix} es': (f'{str(round(min(grade_time_list)/3600,2))}h'),
    f'· El tiempo medio de corrección del lab {lab_prefix} es': (f'{str(round(np.mean(grade_time_list)/3600,2))}h'),
    'Missing PR':missing
    }  
    return dumps(result)


# Purpose: Ranking of the most used memes for datamad0820 divided by labs
@app.route("/lab/memeranking")
def meme_ranking():
    pass


# Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.

@app.route("/lab/<lab>/meme")
def random_meme(lab):
    result=db.pull_request.aggregate([
        { "$match":  {"Lab": lab} },
        { "$sample": {"size": 1} },
        { "$project": { "Url" : 1, "_id": 0}}
      ])
    return dumps(result)