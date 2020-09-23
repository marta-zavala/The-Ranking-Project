from src.app import app
from src.database import db
from flask import request
from ..helpers.json_response_students import asJsonResponseStudents
from bson.json_util import dumps


@app.route('/student/create/<name>')
def create_student(name):
    new_student = {
    'User': name}
    result = db.pull_request.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

@app.route('/student/all')
def list_students():
    res = db.pull_request.distinct('User')
    return (dumps(res))


'''
@app.route("/student/search/<name>")
@asJsonResponseStudents
def search_student(name):
    query = {'User':name}
    result = db.pull_request.find(query)
    return result
'''