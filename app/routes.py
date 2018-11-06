import os
from flask import Flask, request, jsonify, render_template
from app import app

# home route which is a get and post route
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		with open("/tmp/output_file", "bw") as f:
			chunk_size = 4096
			while True:
				chunk = request.stream.read(chunk_size)
				# print(chunk)
				if len(chunk) == 0:
					break
				f.write(chunk)
		
			with open("/tmp/output_file", "br") as f:
				 	print(f.read())

		return jsonify("Successful upload")

	# print("THIS IS WHAT F IS: ", f.name)

	return render_template('index.html')


