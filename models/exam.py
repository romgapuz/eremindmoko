from models.base import db
from models.subject import Subject


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_date = db.Column(db.Date)
    time_range = db.Column(db.String(20))
    room = db.Column(db.String(30))
    subject_id = db.Column(db.Integer(), db.ForeignKey(Subject.id))
    subject = db.relationship(Subject, foreign_keys=[subject_id])

    def __str__(self):
        return '{} ({})'.format(self.subject, self.exam_date)
