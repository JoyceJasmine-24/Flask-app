from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home page"

@app.route("/about")
def about():
    return "This is a simple Flask app"

@app.route("/contact")
def contact():
    return "Contact us joycejasmine342@gmail.com"

@app.route("/services")
def services():
    return "We offer web development and AI Solutions"

@app.route("/help")
def help_page():
    return "How can we help?"

if __name__ == "__main__":
    app.run(debug=True)