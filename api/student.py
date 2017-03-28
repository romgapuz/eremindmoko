from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.student import (
    Student,
    add_student,
    update_student,
    delete_student
)
from schema.student import StudentSchema


def register(app):
    app.add_url_rule(
        '/student/',
        view_func=StudentApi.as_view('student')
    )
    app.add_url_rule(
        '/student/<id>',
        view_func=StudentIdApi.as_view('student_id')
    )


class StudentApi(MethodView):
    def post(self):
        try:
            student_no = request.form['student_no']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            username = request.form['username']
            password = request.form['password']

            item_id = add_student(
                student_no,
                first_name,
                last_name,
                username,
                password
            )

            return '{}'.format(item_id), 201
        except Exception, ex:
            return "Create student failed: {}".format(repr(ex)), 400


class StudentIdApi(MethodView):
    def get(self, id):
        try:
            result = Student.query.filter_by(id=id).one()
            return jsonify(StudentSchema(many=False).dump(result).data)
        except NoResultFound:
            return jsonify(StudentSchema(many=False).dump(None).data), 404
            
    def put(self, id):
        try:
            student_no = request.form['student_no'] \
                if 'student_no' in request.form else None
            first_name = request.form['first_name'] \
                if 'first_name' in request.form else None
            last_name = request.form['last_name'] \
                if 'last_name' in request.form else None
            username = request.form['username'] \
                if 'username' in request.form else None
            password = request.form['password'] \
                if 'password' in request.form else None
        except Exception, ex:
            return "Could not validate user information: {}". \
                format(repr(ex)), 400

        try:
            update_student(
                id,
                student_no,
                first_name,
                last_name,
                username,
                password
            )
        except Exception, ex:
            return "Error updating student: {}". \
                format(repr(ex)), 400

        return jsonify(StudentSchema(many=True).dump(None).data), 200

    def delete(self, id):
        deleted = delete_student(id)
        if deleted:
            return jsonify(StudentSchema(many=True).dump(None).data), 200
        else:
            return "No item deleted", 400
