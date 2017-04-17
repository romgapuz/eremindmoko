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


def delete_exam(id):
    deleted = Exam.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted


@db.event.listens_for(Exam, "after_insert")
def check_exam_date(mapper, connection, target):
    for student in target.subject.students:
        if student.registration_id:
            connection.execute(
                "insert into notification (" +
                "notification_date," +
                "title," +
                "message," +
                "registration_id," +
                "reference_id," +
                "is_sent" +
                ") values (" +
                "'" + str(target.exam_date) + "', " +
                "'Exam', " +
                "'You have an exam today at room {} on {}', ".format(
                    target.room,
                    target.time_range
                ) +
                "'" + student.registration_id + "', " +
                str(target.id) + ", " +
                "0)"
            )
