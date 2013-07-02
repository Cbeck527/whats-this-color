from flask import Flask

app = Flask(__name__)


def isHex(inputValue=""):
    # length test
    if len(inputValue) == 3 or len(inputValue) == 6:
        # expand if shorthand
        if len(inputValue) == 3:
            inputValue = inputValue[0] + inputValue[0] + inputValue[1] + inputValue[1] + inputValue[2] + inputValue[2]
        # check to see if all characters are valid hex
        import string
        if all(c in string.hexdigits for c in inputValue):
            return inputValue
    else:
        return False


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<inputColor>')
def returnColor(inputColor):
    color = isHex(inputColor)
    if color:
        return '<style>body{background-color:#%s;}</style>The color is #%s' % (color, color)
    else:
        return 'Not a valid hex color'

if __name__ == '__main__':
    app.run(debug=True)