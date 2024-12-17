from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'jbcnrajveer@gmail.com'  
app.config['MAIL_PASSWORD'] = 'ohky eijy joxr jlhj'
app.config['MAIL_DEFAULT_SENDER'] = 'jbcnrajveer@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return """
    <h1>Bulk Email Sender</h1>
    <form method="POST" action="/send" enctype="multipart/form-data">
        <label>Email Recipients (comma-separated):</label><br>
        <input type="text" name="recipients" placeholder="example1@gmail.com, example2@gmail.com" size="50"><br><br>
        <label>Email Subject:</label><br>
        <input type="text" name="subject" placeholder="Enter subject" size="50"><br><br>
        <label>Email Body:</label><br>
        <textarea name="body" rows="5" cols="50" placeholder="Enter email body here"></textarea><br><br>
        <button type="submit">Send Bulk Email</button>
    </form>
    """

@app.route('/send', methods=['POST'])
def send_email():
    if request.method == 'POST':
        recipients = request.form['recipients'].split(',')  
        subject = request.form['subject']
        body = request.form['body']

        try:
            msg = Message(subject, recipients=[r.strip() for r in recipients])
            msg.body = body

            mail.send(msg)
            return "<h1>Emails sent successfully!</h1>"
        except Exception as e:
            return f"<h1>Error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
