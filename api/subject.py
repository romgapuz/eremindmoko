from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.subject import (
    Subject,
    add_subject,
    update_subject,
    delete_subject
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
        
    def post(self, id):
        try:
            code = request.form['code']
            description = request.form['description']
            days = request.form['days']
            time_start = datetime.datetime.strptime(request.form['time_start'], '%I:%M %p').time()
            time_end = datetime.datetime.strptime(request.form['time_end'], '%I:%M %p').time()
            section = request.form['section']

            item_id = add_subject(
                code,
                description,
                days,
                time_start,
                time_end,
                section,
                id
            )

            return '{}'.format(item_id), 201
        except Exception, ex:
            return "Create subject failed: {}".format(repr(ex)), 400


class SubjectIdApi(MethodView):
    def get(self, id):
        try:
            result = Subject.query.filter_by(id=id).one()
            return jsonify(SubjectSchema(many=False).dump(result).data)
        except NoResultFound:
            return jsonify(SubjectSchema(many=False).dump(None).data), 404
            
    def put(self, id):
        try:
            code = request.form['code'] \
                if 'code' in request.form else None
            description = request.form['description'] \
                if 'description' in request.form else None
            days = request.form['days'] \
                if 'days' in request.form else None
            time_start = request.form['time_start'] \
                if 'time_start' in request.form else None
            time_end = request.form['time_end'] \
                if 'time_end' in request.form else None
            section = request.form['section'] \
                if 'section' in request.form else None
        except Exception, ex:
            return "Could not validate subject information: {}". \
                format(repr(ex)), 400

        try:
            update_subject(
                id,
                code,
                description,
                days,
                time_start,
                time_end,
                section,
                None
            )
        except Exception, ex:
            return "Error updating subject: {}". \
                format(repr(ex)), 400

        return jsonify(SubjectSchema(many=True).dump(None).data), 200

    def delete(self, id):
        deleted = delete_subject(id)
        if deleted:
            return jsonify(SubjectSchema(many=True).dump(None).data), 200
        else:
            return "No item deleted", 400


class SubjectApi(MethodView):
    def post():
        try:
            code = request.form['code']
            description = request.form['description']
            days = request.form['days']
            time_start = datetime.datetime.strptime(request.form['time_start'], '%I:%M %p').time()
            time_end = datetime.datetime.strptime(request.form['time_end'], '%I:%M %p').time()
            section = request.form['section']

            item_id = add_subject(
                code,
                description,
                days,
                time_start,
                time_end,
                section,
                None
            )

            return '{}'.format(item_id), 201
        except Exception, ex:
            return "Create subject failed: {}".format(repr(ex)), 400

class SubjectIdRegisterApi(MethodView):
    def put(self, id):
        try:
            student_id = request.form['student_id'] \
                if 'student_id' in request.form else None
        except Exception, ex:
            return "Could not validate subject information: {}". \
                format(repr(ex)), 400

        try:
            update_subject(
                id,
                None,
                None,
                None,
                None,
                None,
                None,
                student_id
            )
        except Exception, ex:
            return "Error updating subject: {}". \
                format(repr(ex)), 400

        return jsonify(SubjectSchema(many=True).dump(None).data), 200
