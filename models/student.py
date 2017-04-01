from models.base import db
from models.subject import Subject


student_subject_table = db.Table(
    'student_subject',
    db.Model.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
    course = db.Column(db.String(80))
    year_level = db.Column(db.String(30))
    is_verified = db.Column(db.Boolean)
    subjects = db.relationship(Subject, secondary=student_subject_table)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


def add_student(
        student_no,
        first_name,
        middle_name,
        last_name,
        email,
        password,
        course,
        year_level):
    item = Student()
    item.student_no = student_no
    item.first_name = first_name
    item.middle_name = middle_name
    item.last_name = last_name
    item.email = email
    item.password = password
    item.course = course
    item.year_level = year_level
    item.is_verified = False

    db.session.add(item)
    db.session.commit()

    return item.id


def update_student(
        id,
        student_no,
        first_name,
        middle_name,
        last_name,
        email,
        password,
        course,
        year_level,
        is_verified):
    item = Student.query.filter_by(id=id).one()

    if student_no is not None:
        item.student_no = student_no
    if first_name is not None:
        item.first_name = first_name
    if middle_name is not None:
        item.middle_name = middle_name
    if last_name is not None:
        item.last_name = last_name
    if email is not None:
        item.email = email
    if password is not None:
        item.password = password
    if course is not None:
        item.course = course
    if year_level is not None:
        item.year_level = year_level
    if is_verified is not None:
        item.is_verified = is_verified

    db.session.commit()


def delete_student(id):
    deleted = Student.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted


def register_subject(student_id, subject_id):
    student = Student.query.filter_by(id=student_id).one()
    subject = Subject.query.filter_by(id=subject_id).one()

    item = student.subjects.append(subject)
    db.session.commit()

    return item
