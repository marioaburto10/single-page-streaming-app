# bring in print() if using python2 to run this app
from __future__ import print_function

# bring in dependencies
import tempfile
from flask import Flask, request, jsonify, render_template, send_file
import werkzeug

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
def hello(path):
  if request.method == 'POST':
    print('new request')
    # function that will create a temporary file to store the incoming file in
    def custom_stream_factory(total_content_length, filename, content_type, content_length=None):
        tmpfile = tempfile.NamedTemporaryFile('wb+', prefix='flaskapp')
        print("start receiving file ... filename => " + str(tmpfile.name))
        return tmpfile
    
    # use the standard Werkzeug parsing behavior from the parse_form_data() method to stream the incoming file into a temp file
    # stream will be empty and form will contain the regular POST / PUT data, files will contain the uploaded files as FileStorage objects.
    stream,form,files = werkzeug.formparser.parse_form_data(request.environ, stream_factory=custom_stream_factory)

    # iterate through the keys of the FileStorage object to get the path of the newly streamed file mainly
    for fil in files.values():
        print(" ".join(["saved form name", fil.name, "submitted as", fil.filename, "to temporary file", fil.stream.name]))

        # test to see if file was completely streamed by reading the temp file, only do this if the file is small
        # with open(fil.stream.name, "r") as f:
        #             print(f.read())

    return "Successfully streamed file"
    # return send_file(fil.stream.name,
    #                  mimetype='text/csv',
    #                  attachment_filename='data.csv',
    #                  as_attachment=True)

  return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8090)


