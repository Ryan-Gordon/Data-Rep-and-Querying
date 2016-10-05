from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "Hello Ryan!"

@app.route("/name/<user>")
def helloName(user):
    return "Hello Student {}".format(user)

if __name__ == "__main__":
    app.run()

