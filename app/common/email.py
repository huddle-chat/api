# TODO
from flask_mail import Message
from app.extensions import mail


def send_test_email():
    msg = Message(
        "Hello From Flask",
        sender="huddlechat.io@gmail.com",
        recipients=["mattyard11@gmail.com"]
    )

    msg.body = "This is a test email sent from the Flask app!"

    mail.send(msg)
    return "Email Sent!"


def send_verification_email(email: str, verification_code):
    msg = Message(
        "Your Huddle Verification Code",
        sender="huddlechat.io@gmail.com",
        recipients=[email]
    )

    msg.body = f"""Thanks for signing up for Huddle!
    Your verification code is: {verification_code}"""

    mail.send(msg)
