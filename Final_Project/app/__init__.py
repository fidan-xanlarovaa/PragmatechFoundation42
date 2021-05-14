#app
from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
UPLOAD_FOLDER='app/static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db = SQLAlchemy(app)
migrate=Migrate(app,db)

from app.models import *
from admin.routes import *
from main.routes import *



