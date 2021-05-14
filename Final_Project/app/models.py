from app import db

class About_section(db.Model):
    a_s_id=db.Column(db.Integer,primary_key=True,nullable=False)
    a_s_title=db.Column(db.String(50),nullable=False)
    a_s_description=db.Column(db.Text,nullable=False)
    a_s_link=db.Column(db.String(250),nullable=False)
    a_s_link_title=db.Column(db.String(250),nullable=False)
    a_s_image=db.Column(db.String(250),nullable=False)

class Motivation_word_section(db.Model):
    m_w_id=db.Column(db.Integer,primary_key=True,nullable=False)
    m_w_description=db.Column(db.String(250),nullable=False)




   