from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.subject import Subject
from models.student import (
    Student,
    register_subject
)
from schema.subject import SubjectSchema


def register(app):
    app.add_url_rule(
        '/student/<id>/subject/',
        view_func=StudentIdSubjectApi.as_view('student_id_subject')
    )
    app.add_url_rule(
        '/subject/<id>',
        view_func=SubjectIdApi.as_view('subject_id')
    )
    app.add_url_rule(
        '/subject/',
        view_func=SubjectApi.as_view('subject')
    )
    app.add_url_rule(
        '/subject/<id>/register',
        view_func=SubjectIdRegisterApi.as_view('subject_id_register')
    )


class StudentIdSubjectApi(MethodView):
    def get(self, id):
        try:
            result = Subject.query.filter_by(
                student_id=id
            ).all()
            return jsonify(SubjectSchema(many=True).dump(result).data)
        except NoResultFound:
            return jsonify(SubjectSchema(many=True).dump([]).data), 404


class SubjectIdApi(MethodView):
    def get(self, id):
        try:
            result = Subject.query.filter_by(id=id).one()
            return jsonify(SubjectSchema(many=False).dump(result).data)
        except NoResultFound:
            return jsonify(SubjectSchema(many=False).dump(None).data), 404

    def delete(self, id):
        deleted = delete_subject(id)
        if deleted:
            return jsonify(SubjectSchema(many=True).dump(None).data), 200
        else:
            return "No item deleted", 400


class SubjectApi(MethodView):
    def get(self):
        try:
            result = Subject.query.filter_by(student_id=None).all()
            return jsonify(SubjectSchema(many=True).dump(result).data)
        except NoResultFound:
            return jsonify(SubjectSchema(many=True).dump([]).data), 404


class SubjectIdRegisterApi(MethodView):
    def put(self, id):
        try:
            student_id = request.form['student_id'] \
                if 'student_id' in request.form else None
        except Exception, ex:
            return "Could not validate subject information: {}". \
                format(repr(ex)), 400

        try:
            register_subject(student_id, id)
        except Exception, ex:
            return "Error registering subject: {}". \
                format(repr(ex)), 400

        return jsonify(SubjectSchema(many=True).dump(None).data), 200
