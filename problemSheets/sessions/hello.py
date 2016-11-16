from flask import Flask, render_template, request, make_response
app = Flask(__name__)



# Route takes input based on URL provide /name/Ryan provides the param user
@app.route("/name/<user>")
def helloName(user):
    return "Hello Student {}".format(user)

# Loads a page from the templates folder called index.html
@app.route("/<string:page_name>/")
def template_page(page_name):
    return render_template('%s.html' % page_name)

@app.route("/")
def static_page():
    return render_template('index.html')

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['firstname'] 
    resp = make_response(render_template('index.html'))   
    resp.set_cookie('userID', user)
    return resp
   else:
        return "No Joy!"
   


# This statement must be after the route definitions
# Will cause a breakpoint, or will not render anything below the snippet
if __name__ == "__main__":
    app.run(debug = true)

