from models.base import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notification_date = db.Column(db.Date)
    title = db.Column(db.String(30))
    message = db.Column(db.String(100))
    registration_id = db.Column(db.String(300))
    reference_id = db.Column(db.Integer)
    is_sent = db.Column(db.Boolean)

    def __str__(self):
        return '{} ({})'.format(self.title, self.notification_date)
