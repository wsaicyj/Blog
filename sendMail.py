from flask_mail import Message
from hello import app,mail



msg = Message('test subject',sender='wsaicyj@163.com',recipients=['84160330@qq.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
#mail.send(msg)
with app.app_context():
    mail.send(msg)
