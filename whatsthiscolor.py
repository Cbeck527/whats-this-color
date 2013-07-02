from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<inputColor>')
def returnColor(inputColor):
    return 'The color was #%s' % inputColor

if __name__ == '__main__':
    app.run(debug=True)
