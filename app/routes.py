import os
from flask import Flask, request, jsonify, render_template
from app import app

# home route which is a get and post route
@app.route('/', methods=['GET', 'POST'])
def index():
	# when uploading a file to this flask server, open a temporary file to store the incoming file
	# this avoids storing the incoming file into memory
	if request.method == 'POST':
		with open("/tmp/output_file", "wb") as f:
			chunk_size = 4096
			while True:
				# use the standard Werkzeug parsing behavior method from the request.stream.read() method to stream the incoming file chunk by chunk
				chunk = request.stream.read(chunk_size)
				# if there are no more chunks to process, let the user know that the file was successfully streamed and uploaded
				if len(chunk) == 0:
					break
					# return "File was streamed successfully to the server"
				# write the incoming file chunk by chunk into the temp file	
				f.write(chunk)

		# test to see if the temp file is the same size as the original
		size = os.path.getsize("/tmp/output_file") / 1000000 # output is in bytes so divide by 1e+6 to get MB size
		print("SIZE: ", size)

		# open and read the temp file to see if the file contents were fully streamed
		# only do this if the file is small, otherwise remove these two lines because they will crash the server
		# with open("/tmp/output_file", "br") as f:
		# 	 	print(f.read())
		return "File with size %s MB was streamed successfully to the server" % (size)
	# on initial page load, render an input field that will let the user upload a file
	return render_template('index.html')


