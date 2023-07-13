from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, GitHub Action!'

@app.route('/upDown')
def upDown():
    return 'Hello, upDown!'

if __name__ == '__main__':
    app.run()
