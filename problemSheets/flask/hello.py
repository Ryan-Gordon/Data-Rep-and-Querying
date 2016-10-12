from flask import Flask, render_template, request
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

# Loads a page from the templates folder called index.html
@app.route("/<string:page_name>/")
def template_page(page_name):
    return render_template('%s.html' % page_name)

@app.route("/")
def static_page():
    return current_app.send_static_file('index.html')

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


# This statement must be after the route definitions
# Will cause a breakpoint, or will not render anything below the snippet
if __name__ == "__main__":
    app.run()

