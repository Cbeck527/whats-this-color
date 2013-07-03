from flask import Flask, render_template, send_file, request
from PIL import Image
import StringIO

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

def isDark(inputColor):
    if int(inputColor,16) > 8388607:
        return "000000"
    else:
        return "ffffff"


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<inputColor>')
def returnColor(inputColor):
    color = isHex(inputColor)
    if color:
        textColor = isDark(color)
        return render_template('color.html', color=color, textColor=textColor)
    else:
        return render_template('error.html')

@app.route('/favicon.ico')
def returnFavicon():
    color = request.args.get('color')
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    img = Image.new('RGB', (16, 16), (r, g, b))
    img_io = StringIO.StringIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)