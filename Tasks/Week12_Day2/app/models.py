from app import db
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    p_title=db.Column(db.String(50))
    p_desc=db.Column(db.String(50))
    p_photo=db.Column(db.String(50))