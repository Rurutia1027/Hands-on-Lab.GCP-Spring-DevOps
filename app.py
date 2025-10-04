from flask import Flask 
app = Falsk(__name__)

@app.route('/')
def hello_world(): 
    return 'Hello, Simple Flask application'