from flask import Flask, render_template, request ## 

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

## Entry point of any .py file
if __name__ == "__main__":
    
    app.run(debug=True) 