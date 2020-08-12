from flask import Flask, request, render_template

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


if __name__ == "__main__":
    app.run(debug=True)