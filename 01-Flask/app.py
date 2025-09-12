from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return "Hi, This is home page."


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

# HTTP Verbs: By default is GET
# Ex: google.com -> GET request
# go to google.com and search "Sagar Chhabriya" -> Post Request

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method =="POST":
        name = request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

# Action parameters
@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method =="POST":
        name = request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

# Dynamic URLs and Jinja Templating



# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res =""
    
    if score>50:
        res="PASS"
    else:
        res="FAIL"    
    
    exp = {'score':score, "result": res}

    return render_template("result.html", result=res, marks=score, exp=exp)
# Jinja2 Template Engine
'''
{{ }} expressions to print out in html
{% %} conditions, for loops
{# #} this is for comments 
'''

# Variable Rule
@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result_if.html", result=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', result=score)

@app.route("/submitres", methods=['GET','POST'])
def submit_results():
    total_score = 0

    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c=float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science)/4
    
    return redirect(url_for('submitres', score=total_score))   

if __name__=="__main__":
    app.run(debug=True)