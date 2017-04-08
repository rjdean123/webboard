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
    	return handler.handle_post(raw_coordinates_str)
    else:
    	return 'unsupported http method'

if __name__ == '__main__':
	handler = RequestHandler()
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)