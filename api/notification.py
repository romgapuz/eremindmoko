from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound
import utils.push_check as push_check


def register(app):
    app.add_url_rule(
        '/check',
        view_func=Check.as_view('check')
    )


class Check(MethodView):
    def get(self):
        try:
            sent = push_check.check()
        except NoResultFound:
            return "", 404

        return str(sent)
