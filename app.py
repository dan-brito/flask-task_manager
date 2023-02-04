from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)