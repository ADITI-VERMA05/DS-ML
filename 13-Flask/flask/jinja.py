## Building URL Dynamically
## Variable Rule
## Jinja2 Template Engine

### Jinja2 template engine 
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
from flask import Flask, render_template, request, redirect, url_for ## 

## WSGI application
app = Flask(__name__)

## creating route
@app.route("/") 
def welcome():
    return "<html><H1>Welcome to this Flask Course.</H1></html>"

@app.route("/index", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        # pass
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route("/submit", methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        # pass
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    # return "The marks you got is "+ str(score)
    res=""
    if score >=50:
        res = "passed"
    else:
        res = "failed"
    return render_template('result.html',results = res)

## Variable rule 2
@app.route('/success_res/<int:score>')
def success_res(score):
    res=""
    if score >=50:
        res = "passed"
    else:
        res = "failed"
    exp = {'score':score, "res":res}
    return render_template('result1.html',results = exp)

## if condition
@app.route('/success_if/<int:score>')
def success_if(score):
    return render_template('result2.html',results = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results = score)

@app.route('/get_result', methods=['POST','GET'])
def get_result():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+maths+c+datascience)/4
    else:
        return render_template('get_result.html')
    
    return redirect(url_for('success_res',score=total_score))

## Entry point of any .py file
if __name__ == "__main__":
    
    app.run(debug=True) 
    
    
'''
http://127.0.0.1:5000/success/44
'''