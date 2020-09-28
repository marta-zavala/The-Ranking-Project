from src.app import app
from src.database import db
from flask import request
from ..helpers.json_response_students import asJsonResponseStudents
from bson.json_util import dumps



@app.route('/')
def welcome():
    return '''
<!DOCTYPE html>
<html lang="en">
<center>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ironhack DataLabs</title>
</head>
<body style="background-color:#8FBAB0;">
<h1>Esta API funciona correctamente, para obtener información introduce un endpoint.</h1>
</center>
<div class="block" style="float: right; width: 45%"> 

<h2>Student Endpoints:<h2>
<ul>
    <li>(GET) /student/create/'name'</li>
    <li>(GET) /student/all</li>
    <li>(GET) /student/search/'name'</li>
</ul>
</div>
<div class="block" style="float: right; width: 45%">

<h2>   Lab Endpoints:<h2>
<ul>
    <li>(GET) /lab/create/'name'</li>
    <li>(GET) /lab/'lab_prefix'/search</li>
    <li>(GET) /lab/'lab'/meme</li>
</ul>
</div>
<div style="clear: both"></div>
</dd>
<center>
<img src="https://image.flaticon.com/icons/png/512/1051/1051377.png"/>
<form>
    <input type="button" value="Go back" onclick="history.back()">
</form>
</body>
</html>
'''
    


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
Purpose: Search all pull request of a student
Params: The student name
Returns The student pull request info
'''
@app.route("/student/search/<name>")
@asJsonResponseStudents
def search_student(name):
    query = {'User':name}
    result = db.pull_request.find(query)
    return result
