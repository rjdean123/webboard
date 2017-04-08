import os

from flask import Flask
from flask import request
app = Flask(__name__)

from helpers import RequestHandler

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
    	return handler.handle_get()
    elif request.method == 'POST':
    	raw_coordinates_str = request.form['coordinates']
    	return handler.handle_post(raw_coordinates_str)
    else:
    	return 'unsupported method'

if __name__ == '__main__':
	handler = RequestHandler()
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)