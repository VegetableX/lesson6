from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hellow from github actions'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/Drozhzhin')
def Drozhzhin():
    return 'Hello from CI with GitHub Actions by Drozhzhin'
@app.route('/Drozhzhin2')
def Drozhzhin2():
    return 'Hello from Vegetable Pumpkin!'