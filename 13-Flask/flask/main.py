from flask import Flask, render_template ## for redirecting to html page

'''
It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) Applocation.
'''
## WSGI application
app = Flask(__name__)

## creating route
@app.route("/") ## Decorator >> with first parameter ie. Rule parameter >> '/' is in string format
def welcome():
    return "<html><H1>Welcome to this Flask Course.</H1></html>"

## Any number of routes can be created
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

## Entry point of any .py file
if __name__ == "__main__":
    
    ## Once i created the app, to run it..
    app.run(debug=True) 
    '''debug=True >> enables auto restarting server so that any change in web page is directly visible to 
    the developer while developing, he only needs to save the code and reload the web page, otherwise he was 
    to first save the code then restart the server everytime hemade anty change in the code '''
    
    
'''
OUTPUT:
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 396-426-649
'''