from flask import Flask
from flask import *
import json
# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing
import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 30  # Number of pixels driven from Crickit NeoPixel terminal
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)

def setNeo(r,g,b):
    color = (r, g, b)
    pixels.fill(color)
    pixels.show()

############FLASK
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == "POST":
        r = int(request.form['red'])
        b = int(request.form['blue'])
        g = int(request.form['green'])
        print(r,g,b)
        setNeo(r,g,b)
        return jsonify({'status':'OK','r':r,'g':g, 'b': b})

    else:
        return render_template("neo-example.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
