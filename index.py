from flask import Flask, request, render_template

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string

import config
import os

from boto.s3.connection import S3Connection

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/calculators")
def calculators():
  return render_template("calculators.html")

@app.route("/loans")
def loans():
  return render_template("loans.html")

@app.route("/testimonials")
def testimonials():
  return render_template("testimonials.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/apply")
def apply():
  return render_template("apply.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/calculators/mortgage_calculators")
def mortgage_calculators():
  return render_template("calculators/mortgage_calculators.html")

@app.route("/calculators/principal_calculator")
def principal_calculator():
  return render_template("calculators/principal_calculator.html")

@app.route("/calculators/affordability_calculator")
def affordability_calculator():
  return render_template("calculators/affordability_calculator.html")

@app.route("/report_issue")
def report_issue():
  return render_template("report_issue.html")


@app.route("/loan_programs")
def loan_programs():
  return render_template("loan_programs.html")

@app.route("/form", methods=["GET", "POST"])
def my_form():
    if request.method == 'POST':
        name = request.form.get('name')
        reply_to = request.form.get('email')
        interest = int(request.form.get('interest'))
        print(str(interest))
        outreach = request.form.get('outreach')
        message = request.form.get('message')
        options = ["Refinancing","Purchasing a Home","Loan Programs","Other"]
        print(options[interest])
        send_email(name,reply_to,options[interest],outreach,message)
    return render_template('apply_success.html')

def send_email(name,reply_to,interest,outreach,message):
  mail_content = str(name + " filled out the contact form.\n " + name + " is interested in " + interest + " and found out about this through " + outreach + ".\n " + "Their message is: "
  + message)
  #The mail addresses and password
  sender_address = S3Connection(os.environ['GMAIL_ADDRESS'])
  print(sender_address)
  sender_pass = S3Connection(os.environ['GMAIl_PASSWORD'])
  receiver_address = reply_to
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = name + " filled out the contact form"  #The subject line

  html = """\
  <html>
    <head></head>
    <body>
      <h1>Reply-To:<a href="mailto:{receiver_address}"\>Sender Email</a></h1>
    </body>
  </html>
  """.format(receiver_address=receiver_address)

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(mail_content, 'plain')
  part2 = MIMEText(html, 'html')

  #The body and the attachments for the mail
  message.attach(part1)
  message.attach(part2)
  #Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
  session.starttls() #enable security
  session.login(sender_address, sender_pass) #login with mail_id and password
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')

if __name__ == "__main__":
    app.run(debug=True)