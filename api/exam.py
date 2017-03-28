from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.exam import (
    Exam,
    add_exam,
    update_exam,
    delete_exam
)
from schema.exam import ExamSchema


def register(app):
    app.add_url_rule(
        '/student/<id>/exam/',
        view_func=StudentIdExamApi.as_view('student_id_exam')
    )
    app.add_url_rule(
        '/exam/<id>',
        view_func=ExamIdApi.as_view('exam_id')
    )


class StudentIdExamApi(MethodView):
    def get(self, id):
        try:
            result = Exam.query.filter_by(
                student_id=id
            ).all()
            return jsonify(ExamSchema(many=True).dump(result).data)
        except NoResultFound:
            return jsonify(ExamSchema(many=True).dump([]).data), 404
        
    def post(self, id):
        try:
            subject = request.form['subject']
            exam_date = datetime.datetime.strptime(request.form['exam_date'], "%m/%d/%Y").date()
            time_start = datetime.datetime.strptime(request.form['time_end'], '%I:%M %p').time()
            time_end = datetime.datetime.strptime(request.form['time_end'], '%I:%M %p').time()
            room = request.form['room']

            item_id = add_exam(
                subject,
                exam_date,
                time_start,
                time_end,
                room,
                id
            )

            return '{}'.format(item_id), 201
        except Exception, ex:
            return "Create exam failed: {}".format(repr(ex)), 400


class ExamIdApi(MethodView):
    def get(self, id):
        try:
            result = Exam.query.filter_by(id=id).one()
            return jsonify(ExamSchema(many=False).dump(result).data)
        except NoResultFound:
            return jsonify(ExamSchema(many=False).dump(None).data), 404
            
    def put(self, id):
        try:
            subject = request.form['subject'] \
                if 'subject' in request.form else None
            exam_date = request.form['exam_date'] \
                if 'exam_date' in request.form else None
            time_start = request.form['time_start'] \
                if 'time_start' in request.form else None
            time_end = request.form['time_end'] \
                if 'time_end' in request.form else None
            room = request.form['room'] \
                if 'room' in request.form else None
        except Exception, ex:
            return "Could not validate exam information: {}". \
                format(repr(ex)), 400

        try:
            update_exam(
                id,
                subject,
                exam_date,
                time_start,
                time_end,
                room
            )
        except Exception, ex:
            return "Error updating exam: {}". \
                format(repr(ex)), 400

        return jsonify(ExamSchema(many=True).dump(None).data), 200

    def delete(self, id):
        deleted = delete_exam(id)
        if deleted:
            return jsonify(ExamSchema(many=True).dump(None).data), 200
        else:
            return "No item deleted", 400
