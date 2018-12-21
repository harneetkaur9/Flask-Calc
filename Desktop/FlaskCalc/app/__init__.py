#Flask application instance
from flask import Flask

#create app
app = Flask(__name__)

from app import routes
