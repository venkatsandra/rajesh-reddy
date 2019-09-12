from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "sandrasoft.py@gmail.com",
    "MAIL_PASSWORD": "143143@sv"
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route("/email")
def email_send():
	msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["raimasthanreddy@gmail.com"], # replace with your email for testing
                      body=" Iam sending email with flask this is testing.")
	mail.send(msg)
	return "An email has been send to your  accout"

if __name__ == "__main__":
	app.run(debug=True)