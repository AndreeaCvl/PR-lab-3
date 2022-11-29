from flask import Flask, make_response, jsonify, request
from functions import *

app = Flask(__name__)


# get all students
@app.route('/api/students', methods=['GET'])
def get_students():
    return make_response(jsonify(fetch_db_all()), 200)


# add a student
@app.route('/api/students', methods=['POST'])
def add_students():
    post_data = request.get_json()
    return jsonify(add_student(post_data))


# get student by id
@app.route('/api/students/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    return jsonify(fetch_db(student_id))


# update student by id
@app.route('/api/students/update', methods=['PUT'])
def update_student_by_id():
    student = request.get_json()
    return jsonify(update_student(student))


@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student_by_id(student_id):
    return jsonify(delete_student(student_id))


if __name__ == '__main__':
    app.run()