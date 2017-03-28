from flask import jsonify
from flask.views import MethodView
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from models.announcement import Announcement
from schema.announcement import AnnouncementSchema


def register(app):
    app.add_url_rule(
        '/announcement/',
        view_func=AnnouncementApi.as_view('announcement')
    )


class AnnouncementApi(MethodView):
    def get(self):
        try:
            result = Announcement.query.filter_by().order_by("log_date desc").all()
            return jsonify(AnnouncementSchema(many=True).dump(result).data)
        except NoResultFound:
            return jsonify(AnnouncementSchema(many=True).dump([]).data), 404
