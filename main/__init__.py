import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os




app = Flask(__name__)


from main import routes

print(sys.path)
print(pd.__version__)
app.app_context().push()