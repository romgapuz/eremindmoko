from models.base import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    description = db.Column(db.String(100))
    days = db.Column(db.String(20))
    time_start = db.Column(db.Time)
    time_end = db.Column(db.Time)
    section = db.Column(db.String(30))

    def __str__(self):
        return '({}) {}'.format(self.code, self.description)
