from sqlalchemy.orm.exc import NoResultFound
from models.notification import Notification
from utils.push_sender import PushSender
from datetime import datetime


def check():
    items = Notification.query.filter_by(
        notification_date=datetime.now().date()
    ).all()

    if not items:
        raise NoResultFound

    sender = PushSender()
    for item in items:
        sender.send_single_notification(
            item.registration_id,
            item.title,
            item.message)

    return len(items)
