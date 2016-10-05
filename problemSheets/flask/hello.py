from flask import Flask
app = Flask(__name__)

# Hello
@app.route("/")
def hello():
    return "Hello World!"

# Simple hello function
@app.route("/name")
def name():
    return "Hello Ryan!"

# Route takes input based on URL provide /name/Ryan provides the param user
@app.route("/name/<user>")
def helloName(user):
    return "Hello Student {}".format(user)

@app.route("/signup")
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")

# This statement must be after the route definitions
# Will cause a breakpoint, or will not render anything below the snippet
if __name__ == "__main__":
    app.run()

