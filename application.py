#!usr/bin/python
from flask import Flask, jsonify, render_template
import os
import sys
sys.path.append('static')
from main import getOptimalRoute

application = Flask(__name__,static_folder='static')


@application.route('/', methods=['GET'])
def baseHtml():
    #return application.send_static_file('index.html')
    return render_template('index.html')
@application.route('/q/<string:r>', methods=['GET'])
def index(r):
    [start, destination] = r.split('&')
    polyL = getOptimalRoute(start, destination)
    return jsonify({"points": [start, destination],  "polyline": polyL})

if __name__ == '__main__':
    application.run(debug=True)
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
