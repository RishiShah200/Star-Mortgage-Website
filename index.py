from flask import Flask, request, render_template

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string

import os

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/calculators")
def calculators():
  return render_template("calculators.html")

@app.route("/admin/login")
def login():
  return render_template("admin/login.html")

@app.route("/admin/dashboard")
def dashboard():
  return render_template("admin/dashboard.html")

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

@app.route("/calculators/interest_only_calculator")
def interest_only_calculator():
  return render_template("calculators/interest_only_calculator.html")

@app.route("/calculators/extra_payment_calculator")
def extra_payment_calculator():
  return render_template("calculators/extra_payment_calculator.html")


@app.route("/calculators/tax_benefits_buying")
def tax_benefits_buying():
  return render_template("calculators/tax_benefits_buying.html")

@app.route("/calculators/my_apr")
def my_apr():
  return render_template("calculators/my_apr.html")

@app.route("/home_subpages/purchase_a_home")
def purchase_a_home():
  return render_template("home_subpages/purchase_a_home.html")

@app.route("/home_subpages/refinance")
def refinance():
  return render_template("home_subpages/refinance.html")

@app.route("/report_issue")
def report_issue():
  return render_template("report_issue.html")


@app.route("/loan_programs")
def loan_programs():
  return render_template("loan_programs.html")

@app.route("/faq")
def faq():
  return render_template("faq.html")

@app.route("/form", methods=["GET", "POST"])
def my_form():
    if request.method == 'POST':
        name = request.form.get('name')
        reply_to = request.form.get('email')
        print(request.form.get('interest'))
        interest = int(request.form.get('interest'))
        # print(str(interest))
        outreach = request.form.get('outreach')
        message = request.form.get('message')
        options = ["Refinancing","Purchasing a Home","Loan Programs","Other"]
        # print(options[interest])
        send_email(name,reply_to,options[interest],outreach,message)
    return render_template('apply_success.html')

@app.route("/basic_form", methods=["GET", "POST"])
def my_basic_form():
    if request.method == 'POST':
        name = request.form.get('name')
        reply_to = request.form.get('email')
        send_basic_email(name,reply_to)
    return render_template('apply_success.html')

@app.route("/report_issue_contact", methods=["GET", "POST"])
def report_issue_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        reply_to = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        report_issue_email(name,reply_to,subject,message)
    return render_template('apply_success.html')

def report_issue_email(name,reply_to,subject,message):
  # os.environ["GMAIL_ADDRESS"] = "hahsihsri@gmail.com" #need to set local environment variable. This exists on heroku but not local which is why it doesnt work.
  # os.environ["GMAIL_PASSWORD"] = "Musicisawesome0421"
  mail_content = str(name + " filled out the report issue form.\n" + "They are reporting " + subject + ".\n" + "Their message is: \n" + message)
  #The mail addresses and password
  sender_address = os.environ.get('GMAIL_ADDRESS')
  print(sender_address)
  sender_pass = os.environ.get('GMAIL_PASSWORD')
  print(sender_pass)
  receiver_address = reply_to
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = "Star Mortgage"
  message['To'] = receiver_address
  message['Subject'] = name + " filled out the report issue form"  #The subject line

  html = """\
  <html>
    <head></head>
    <body>
      <h1>Reply-To:<a href="mailto:{receiver_address}"\>{receiver_address}</a></h1>
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

def send_basic_email(name,reply_to):
  # os.environ["GMAIL_ADDRESS"] = "hahsihsri@gmail.com" #need to set local environment variable. This exists on heroku but not local which is why it doesnt work.
  # os.environ["GMAIL_PASSWORD"] = "Musicisawesome0421"
  mail_content = str(name + " filled out the contact form.\n ")
  #The mail addresses and password
  sender_address = os.environ.get('GMAIL_ADDRESS')
  print(sender_address)
  sender_pass = os.environ.get('GMAIL_PASSWORD')
  print(sender_pass)
  receiver_address = reply_to
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = "Star Mortgage"
  message['To'] = receiver_address
  message['Subject'] = name + " filled out the contact form"  #The subject line

  html = """\
  <html>
    <head></head>
    <body>
      <h1>Reply-To:<a href="mailto:{receiver_address}"\>{receiver_address}</a></h1>
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

def send_email(name,reply_to,interest,outreach,message):
  # os.environ["GMAIL_ADDRESS"] = "hahsihsri@gmail.com" #need to set local environment variable. This exists on heroku but not local which is why it doesnt work.
  # os.environ["GMAIL_PASSWORD"] = "Musicisawesome0421"
  mail_content = str(name + " filled out the contact form.\n " + name + " is interested in " + interest + " and found out about this through " + outreach + ".\n " + "Their message is: "
  + message)
  #The mail addresses and password
  sender_address = os.environ.get('GMAIL_ADDRESS')
  print(sender_address)
  sender_pass = os.environ.get('GMAIL_PASSWORD')
  print(sender_pass)
  receiver_address = reply_to
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = "Star Mortgage"
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
    