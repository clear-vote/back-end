from flask import Flask, jsonify, request
from flask_cors import CORS
import json #, send_from_directory

app = Flask(__name__)
# Sends JSON
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://clearvote.info"]}})

@app.route('/')
def hello_world():
	longitude = request.args.get('longitude', type=float)
	latitude = request.args.get('latitude', type=float)
	
	if longitude == 0 and latitude == 0:
		with open('data/test.json', 'r') as file:
			data = json.load(file)  # ?longitude=0&latitude=0
		return jsonify(data)
	else:
		return jsonify({"instructions": "Please set both longitude and latitude to 0 to view the data."})

if __name__ == "__main__":
	# Turn off debug in production
	app.run(debug=True)
	# app.run()
