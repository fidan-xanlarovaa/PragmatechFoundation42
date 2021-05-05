from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    u_name=db.Column(db.String(70))



@app.route('/')
def index():
    return 'Calis kopekkkk'

if __name__=='__main__':
    app.run(debug=True)