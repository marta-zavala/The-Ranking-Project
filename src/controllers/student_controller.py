from src.app import app
from src.database import db
from flask import request
from ..helpers.json_response_students import asJsonResponseStudents
from bson.json_util import dumps

'''
Purpose: Create a student and save into DB
Params: The student name
Returns: The student_id
'''
@app.route('/student/create/<name>')
def create_student(name):
    new_student = {
    'User': name}
    result = db.pull_request.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

'''
Purpose: List all students in database
Returns: An array of student objects
'''
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