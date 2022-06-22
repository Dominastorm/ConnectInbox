from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/result', methods = ['GET', 'POST'])

def connection():
    query = request.get_json()

    if len(query.keys()) < 2:
        return {"Status": "Invalid"}
    
    email = query.get('email')
    password = query.get('password')

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(email, password)
        sent_subject = "Test Email"
        sent_body = "Test Email"
        email_text = """\
        From: %s\r\n 
        %s\r\n

        %s
        """ % (email, sent_subject, sent_body)
        s.sendmail(email, "testwinbox@gmail.com", email_text)
        s.quit()

        return {"Status" : "Success"}
    except:
        return {"Status" : "Failure"}

if __name__ == '__main__':
    app.run(debug=True, port=2000)