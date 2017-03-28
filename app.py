import os
import os.path as op
from flask import Flask
from schema.base import ma
from models.base import db
import api.student as api_student
import api.subject as api_subject
import api.exam as api_exam
import api.announcement as api_announcement
import admin

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = 'd6550c610e95438e8e302d4b312b0a5e'

# Create in-memory database
app.config['DATABASE_FILE'] = 'eremindmoko.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

# Schema
ma.app = app
ma.init_app(app)

# api and admin registration
api_student.register(app)
api_subject.register(app)
api_exam.register(app)
api_announcement.register(app)
admin.register(app, db)


def build_sample_db():
    db.drop_all()
    db.create_all()

    db.session.commit()
    return


if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True)
