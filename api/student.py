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
    app.add_url_rule(
        '/login/',
        view_func=LoginApi.as_view('login')
    )
    app.add_url_rule(
        '/student/<id>/verify',
        view_func=StudentIdVerifyApi.as_view('student_id_verify')
    )


class StudentApi(MethodView):
    def post(self):
        try:
            student_no = request.form['student_no']
            first_name = request.form['first_name']
            middle_name = request.form['middle_name']
            last_name = request.form['last_name']
            password = request.form['password']
            course = request.form['course']
            year_level = request.form['year_level']

            item_id = add_student(
                student_no,
                first_name,
                middle_name,
                last_name,
                password,
                course,
                year_level
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
            middle_name = request.form['middle_name'] \
                if 'middle_name' in request.form else None
            last_name = request.form['last_name'] \
                if 'last_name' in request.form else None
            password = request.form['password'] \
                if 'password' in request.form else None
            course = request.form['course'] \
                if 'course' in request.form else None
            year_level = request.form['year_level'] \
                if 'year_level' in request.form else None
        except Exception, ex:
            return "Could not validate user information: {}". \
                format(repr(ex)), 400

        try:
            update_student(
                id,
                student_no,
                first_name,
                middle_name,
                last_name,
                password,
                course,
                year_level
            )
        except Exception, ex:
            return "Error updating student: {}". \
                format(repr(ex)), 500

        return jsonify(StudentSchema(many=True).dump(None).data), 200

    def delete(self, id):
        deleted = delete_student(id)
        if deleted:
            return jsonify(StudentSchema(many=True).dump(None).data), 200
        else:
            return "No item deleted", 400


class LoginApi(MethodView):
    def post(self):
        try:
            student_no = request.form['student_no']
            password = request.form['password']
        except Exception, ex:
            return "Could not validate student_no and password: {}". \
                format(repr(ex)), 400

        try:
            item = Student.query.filter_by(
                student_no=student_no,
                is_verified=True
            ).one()

            if item.password != password:
                return "Incorrect password", 403
        except Exception:
            return "Student no not found or verified", 403

        return str(item.id)

class StudentIdVerifyApi(MethodView):
    def get(self, id):
        try:
            item = Student.query.filter_by(
                id=id,
                is_verified=False
            ).one()
        except Exception:
            return "Student no not found or already verified", 403

        try:
            update_student(
                id,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                True
            )
        except Exception, ex:
            return "Error verifying student: {}". \
                format(repr(ex)), 500

        return "Student verified successfully"