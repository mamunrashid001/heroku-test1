from flask import Flask
app = Flask(__name__)

@app.route('/')
def index ():
  return 'mamuns first heorku app says hello'
