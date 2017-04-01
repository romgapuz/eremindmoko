import smtplib
import ConfigParser
import os


class EmailSender(object):
    def read_config(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        config = ConfigParser.ConfigParser()
        configfile = os.path.join(ROOT_DIR, '..', 'app.ini')
        config.read(configfile)

        return config

    def send_verification(self, id, email, first_name):
        try:
            config = self.read_config()
        except Exception, ex:
            return "Error reading config file (app.ini): {}". \
                format(repr(ex)), 500

        # get config entries
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
            "Subject: eRemindMoKo Account Verification",
            "",
            "Hi " + first_name,
            "",
            "Thank you for registering at eRemindMoKo. " + \
            "Please verify your account by clicking this link: " + \
            "http://" + app_host + "/student/" + str(id) + "/verify",
            "",
            "Regards,",
            "",
            "eRemindMoKo Team"
        ])
        server.sendmail(sender, email, message_body)
        server.quit()
