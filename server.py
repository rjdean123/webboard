import os

from flask import Flask
from flask import request
from flask import render_template

from flask_cors import CORS

from helpers import RequestHandler

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def board():
    if request.method == 'GET':
    	return render_template("board.html")
    else:
    	return 'unsupported http method'

@app.route("/api", methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
    	return handler.handle_get()
    elif request.method == 'POST':
    	raw_coordinates_str = request.form['coordinates']
    	phone_width = request.form['width']
    	phone_height = request.form['height']
    	return handler.handle_post(raw_coordinates_str, phone_width, phone_height)
    else:
    	return 'unsupported http method'

@app.route("/clear", methods=['DELETE'])
def clear():
    if request.method == 'DELETE':
    	return handler.handle_clear()
    else:
    	return 'unsupported http method'

if __name__ == 'server':
    handler = RequestHandler()
    app.debug = True
	#port = int(os.environ.get("PORT", 5000))
	#app.run(host='0.0.0.0', port=port)