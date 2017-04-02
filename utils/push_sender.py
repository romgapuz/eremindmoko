from pyfcm import FCMNotification
from utils.config import read_config


class PushSender(object):
    def send_single_notification(self, registration_id, title, message):
        # get config entries
        config = read_config()
        server_key = config.get('fcm', 'server_key')

        push_service = FCMNotification(api_key=server_key)
        result = push_service.notify_single_device(
            registration_id=registration_id,
            message_title=title,
            message_body=message
        )

        print result
