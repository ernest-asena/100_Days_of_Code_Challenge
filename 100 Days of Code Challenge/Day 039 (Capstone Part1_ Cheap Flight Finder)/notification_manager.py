from twilio.rest import Client
import config

TWILIO_SID = config.TWILIO_SECOND_SID
TWILIO_AUTH_TOKEN = config.TWILIO_SECOND_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = config.TWILIO_SECOND_NUMBER
TWILIO_VERIFIED_NUMBER = config.TWILIO_VERIFIED_PHONE_TWO


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        """Initializes the class with Twilio client."""
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Sends an SMS with the deal flight details."""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
