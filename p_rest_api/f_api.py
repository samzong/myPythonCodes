#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from bmap_api import getlnglat
import json

app = Flask(__name__)

@app.route('/todo/api/v2.0/alex', methods=['GET'])
def hello():
	return jsonify({'alex':'hello, world.'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v2.0/alex/cityandprice',methods=['GET'])
def cityandprice():
    file = open(r'./cityandprice.json', 'r')
    return file.read()
    file.close()


@app.route('/signUp')
def signUp():
    file = open(r'./cityandprice.json', 'r')
    return file.read()
    file.close()

if __name__ == '__main__':
    app.run(debug=True)
