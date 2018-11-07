from flask import Flask, request, jsonify, render_template
from app import app

# home route which is a get and post route
@app.route('/', methods=['GET', 'POST'])
def index():
	# when uploading a file to this flask server, open a temporary file to store the incoming file
	# this avoids storing the incoming file into memory
	if request.method == 'POST':
		with open("/tmp/output_file", "bw") as f:
			chunk_size = 4096
			while True:
				# use the standard Werkzeug parsing behavior method from the request.stream.read() method to stream the incoming file chunk by chunk
				chunk = request.stream.read(chunk_size)
				# if there are no more chunks to process, let the user know that the file was successfully streamed and uploaded
				if len(chunk) == 0:
					return "File was streamed successfully to the server"
				# write the incoming file chunk by chunk into the temp file	
				f.write(chunk)

			# open and read the temp file to see if the file was fully streamed
			# only do this if the file is small, otherwise remove these two lines because they will crash the server
			with open("/tmp/output_file", "br") as f:
				 	print(f.read())
	# on initial page load, render an input field that will let the user upload a file
	return render_template('index.html')


