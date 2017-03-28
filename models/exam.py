from models.base import db
from models.student import Student


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    exam_date = db.Column(db.Date)
    time_range = db.Column(db.String(20))
    room = db.Column(db.String(30))
    student_id = db.Column(db.Integer(), db.ForeignKey(Student.id))
    student = db.relationship(Student, backref='exams')

    def __str__(self):
        return '{} ({})'.format(self.subject, self.exam_date)


def add_exam(
        subject,
        exam_date,
        time_range,
        room,
        student_id):
    item = Exam()
    item.subject = subject
    item.exam_date = exam_date
    item.time_range = time_range
    item.room = room
    item.student_id = student_id

    db.session.add(item)
    db.session.commit()

    return item.id


def update_exam(
        id,
        subject,
        exam_date,
        time_range,
        room):
    item = Exam.query.filter_by(id=id).one()

    if subject is not None:
        item.subject = subject
    if exam_date is not None:
        item.exam_date = exam_date
    if time_range is not None:
        item.time_range = time_range
    if room is not None:
        item.room = room

    db.session.commit()


def delete_exam(id):
    deleted = Exam.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted
