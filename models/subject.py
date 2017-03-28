from models.base import db
from models.student import Student


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    description = db.Column(db.String(100))
    days = db.Column(db.String(20))
    time_start = db.Column(db.Time)
    time_end = db.Column(db.Time)
    section = db.Column(db.String(30))
    student_id = db.Column(db.Integer(), db.ForeignKey(Student.id))
    student = db.relationship(Student, backref='subjects')

    def __str__(self):
        return '({}) {}'.format(self.code, self.description)


def add_subject(
        code,
        description,
        days,
        time_start,
        time_end,
        section,
        student_id):
    item = Subject()
    item.code = code
    item.description = description
    item.days = days
    item.time_start = time_start
    item.time_end = time_end
    item.section = section
    if student_id is not None:
        item.student_id = student_id

    db.session.add(item)
    db.session.commit()

    return item.id


def update_subject(
        id,
        code,
        description,
        days,
        time_start,
        time_end,
        section,
        student_id):
    item = Subject.query.filter_by(id=id).one()
    
    if code is not None:
        item.code = code
    if description is not None:
        item.description = description
    if days is not None:
        item.days = days
    if time_start is not None:
        item.time_start = time_start
    if time_end is not None:
        item.time_end = time_end
    if section is not None:
        item.section = section
    if student_id is not None:
        item.student_id = student_id

    db.session.commit()


def delete_subject(id):
    deleted = Subject.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted
