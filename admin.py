import flask_admin as admin
from flask_admin.contrib import sqla
from models.student import Student
from models.subject import Subject
from models.exam import Exam
from models.announcement import Announcement


def register(app, db):
    # create admin
    admin_view = admin.Admin(app, name='eRemindMoKo', template_mode='bootstrap3')

    # add views
    admin_view.add_view(sqla.ModelView(Student, db.session))
    admin_view.add_view(sqla.ModelView(Subject, db.session))
    admin_view.add_view(sqla.ModelView(Exam, db.session))
    admin_view.add_view(sqla.ModelView(Announcement, db.session))
