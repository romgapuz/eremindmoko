import smtplib
from utils.config import read_config


class EmailSender(object):
    def send_verification(self, id, email, first_name):
        # get config entries
        config = read_config()
        app_host = config.get('app', 'host')
        email_host = config.get('gmail', 'host')
        sender = config.get('gmail', 'sender')
        username = config.get('gmail', 'username')
        password = config.get('gmail', 'password')

        # send email
        server = smtplib.SMTP(email_host)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        message_body = "\r\n".join([
            "From: " + sender,
            "To: " + email,
            "Subject: eKonek Account Verification",
            "",
            "Hi " + first_name,
            "",
            "Thank you for registering at eKonek. " +
            "Please verify your account by clicking this link: " +
            "http://" + app_host + "/customer/" + str(id) + "/verify",
            "",
            "Regards,",
            "",
            "eKonek Team"
        ])
        server.sendmail(sender, email, message_body)
        server.quit()
