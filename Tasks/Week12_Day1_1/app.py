from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from sqlalchemy.orm import lazyload


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
db = SQLAlchemy(app)



class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    counry_name=db.Column(db.String(50))
    country_states=db.relationship('State',backref='country')

class State(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    state_name=db.Column(db.String(50))
    country_id=db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)



@app.route('/',methods=['GET','POST'])
def index():
    countries=Country.query.all()
    if request.method=='POST':
        selected_country_id=int(request.form['country'])
        states=State.query.filter_by(country_id=selected_country_id)
        return render_template('index.html',countries=countries,states=states)
    return render_template('index.html',countries=countries)


@app.route('/country/add',methods=['GET','POST'])
def add_country():
    if request.method=='POST':
        country=Country(counry_name=request.form['country_name'])
        db.session.add(country)
        db.session.commit()
        return redirect('/')
    return render_template('add_country.html')

@app.route('/state/add',methods=['GET','POST'])
def add_state():
    countries=Country.query.all()
    if request.method=='POST':
        state=State(
             state_name=request.form['state_name'],
             country_id=int(request.form['country_name'])
        )
        db.session.add(state)
        db.session.commit()
        return redirect('/')
    
    return render_template('add_state.html',countries=countries)

if __name__ == '__main__':
    app.run(port=5000,debug=True)