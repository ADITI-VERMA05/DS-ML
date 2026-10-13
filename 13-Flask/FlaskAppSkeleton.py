''' Basic Skeleton '''
from flask import Flask

'''
It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) Applocation.
'''
## WSGI application
app = Flask(__name__)



## Entry point of any .py file
if __name__ == "__main__":
    
    ## Once i created the app, to run it..
    app.run()