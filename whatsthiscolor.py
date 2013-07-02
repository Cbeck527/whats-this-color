from flask import Flask

app = Flask(__name__)


def isHex(inputValue=""):
    if len(inputValue) == 3 or len(inputValue) == 6:
        return True
    else:
        return False


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<inputColor>')
def returnColor(inputColor):
    if isHex(inputColor):
        return 'The color was #%s' % inputColor
    else:
        return 'Not a valid hex color'

if __name__ == '__main__':
    app.run(debug=True)
