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
    user_username=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_password=db.Column(db.String(16))
    user_adress=db.Column(db.String(150))
    user_adress1=db.Column(db.String(150))
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
    countries=Country.query.all()
    if request.method=='POST':
        selected_country_id=int(request.form['country'])
        states=State.query.filter_by(country_id=selected_country_id)
        user= User(
            user_name=request.form['name']
            user_surname=request.form['surname']
            user_username=request.form['username']
            user_email=request.form['email']
            user_pasword=request.form['password']
            user_adress=request.form['adress']
            user_adress1=request.form['adress1']
            country_id=request.form['country']
            state_id=request.form['city ']
        )
        return redirect('/')

@app.route('/',methods=['GET','POST'])
def add_state():
    
    if request.method=='POST':
        
        return render_template('index.html',countries=countries,states=states)
    return render_template('index.html',countries=countries)



if __name__ == '__main__':
    app.run(port=5000,debug=True)

#local storage nedir?