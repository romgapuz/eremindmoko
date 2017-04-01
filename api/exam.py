from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.exam import Exam
from schema.exam import ExamSchema


def register(app):
    app.add_url_rule(
        '/subject/<id>/exam/',
        view_func=SubjectIdExamApi.as_view('subject_id_exam')
    )
    app.add_url_rule(
        '/exam/<id>',
        view_func=ExamIdApi.as_view('exam_id')
    )


class SubjectIdExamApi(MethodView):
    def get(self, id):
        try:
            result = Exam.query.filter_by(
                subject_id=id
            ).all()
            return jsonify(ExamSchema(many=True).dump(result).data)
        except NoResultFound:
            return jsonify(ExamSchema(many=True).dump([]).data), 404


class ExamIdApi(MethodView):
    def get(self, id):
        try:
            result = Exam.query.filter_by(id=id).one()
            return jsonify(ExamSchema(many=False).dump(result).data)
        except NoResultFound:
            return jsonify(ExamSchema(many=False).dump(None).data), 404
