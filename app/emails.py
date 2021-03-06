from .decorators import async
from flask import render_template
from config import ADMINS
from flask.ext.mail import Message
from app import mail

@async
def send_sync_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,sender,recipients,text_body,html_body):
    msg = Message(subject,sender=sender,recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    thr = thread(target=send_async_email, args=[current_app,msg])
    thr.start()

def follower_notification(followed,follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt",
            user=followed, follower=follower),
        render_template("follower_email.html",
            user=followed,follower=follower))
