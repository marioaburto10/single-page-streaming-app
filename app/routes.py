import os
from flask import Flask, request, jsonify, render_template
from app import app

# home route which is a get and post route
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':

		if request.files.get('file'):
			# read the file
			file = request.files['file']

			# read the filename
			filename = file.filename

			# create a path to the uploads folder
			# filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

			# Save the file to the uploads folder
			# file.save(filepath)

			return jsonify(filename)

	return render_template('index.html')


