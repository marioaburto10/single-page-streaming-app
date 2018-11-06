from flask import Flask

app = Flask(__name__)
# point to uploads folder incase we want to save the files we are uploading
app.config['UPLOAD_FOLDER'] = 'uploads'

# bring in the routes, currently only one index route
from app import routes
