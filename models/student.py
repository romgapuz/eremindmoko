from models.base import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(80))
    course = db.Column(db.String(80))
    year_level = db.Column(db.String(10))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


def add_student(
        student_no,
        first_name,
        middle_name,
        last_name,
        password,
        course,
        year_level):
    item = Student()
    item.student_no = student_no
    item.first_name = first_name
    item.middle_name = middle_name
    item.last_name = last_name
    item.password = password
    item.course = course
    item.year_level = year_level

    db.session.add(item)
    db.session.commit()

    return item.id


def update_student(
        id,
        student_no,
        first_name,
        middle_name,
        last_name,
        password,
        course,
        year_level):
    item = Student.query.filter_by(id=id).one()

    if student_no is not None:
        item.student_no = student_no
    if first_name is not None:
        item.first_name = first_name
    if middle_name is not None:
        item.middle_name = middle_name
    if last_name is not None:
        item.last_name = last_name
    if password is not None:
        item.password = password
    if course is not None:
        item.course = course
    if year_level is not None:
        item.year_level = year_level

    db.session.commit()


def delete_student(id):
    deleted = Student.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted
