from models.base import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_no = db.Column(db.String(20))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


def add_student(
        student_no,
        first_name,
        last_name,
        username,
        password):
    item = Student()
    item.student_no = student_no
    item.first_name = first_name
    item.last_name = last_name
    item.username = username
    item.password = password

    db.session.add(item)
    db.session.commit()

    return user.id


def update_student(
        id,
        student_no,
        first_name,
        last_name,
        username,
        password):
    item = Student.query.filter_by(id=id).one()

    if student_no is not None:
        item.student_no = student_no
    if first_name is not None:
        item.first_name = first_name
    if last_name is not None:
        item.last_name = last_name
    if username is not None:
        item.username = username
    if password is not None:
        item.password = password

    db.session.commit()


def delete_student(id):
    deleted = Student.query.filter_by(id=id).delete()
    db.session.commit()
    return deleted
