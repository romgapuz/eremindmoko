from models.base import db


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_date = db.Column(db.Date)
    content = db.Column(db.String(100))

    def __str__(self):
        return '{} {}'.format(self.log_date)
