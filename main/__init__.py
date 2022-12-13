import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


from main import routes

print(sys.path)
app.app_context().push()