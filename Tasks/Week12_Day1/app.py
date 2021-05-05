from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import lazyload


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
db = SQLAlchemy(app)
migrate=Migrate(app,db)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_surname=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_pasword=db.Column(db.String(16))
    country_id=db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)
    state_id=db.Column(db.Integer, db.ForeignKey('state__.id'),nullable=False)



class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    counry_name=db.Column(db.String(50))
    country_states=db.relationship('State',backref='country')

class State(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    state_name=db.Column(db.String(50))
    country_id=db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)
    state__=db.relationship('User',backref='state__')


@app.route('/',methods=['GET','POST'])
def add_state():
    return "calis kopekkk"



if __name__ == '__main__':
    app.run(port=5000,debug=True)

#local storage nedir?