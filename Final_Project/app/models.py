from app import db
class Slider_section(db.Model):
    s_id=db.Column(db.Integer,primary_key=True,nullable=False)
    s_title=db.Column(db.String(50),nullable=False)
    s_description=db.Column(db.String(250),nullable=False)
    s_link=db.Column(db.String(250),nullable=False)
    s_link_title=db.Column(db.String(250),nullable=False) 
    s_image=db.Column(db.String(250),nullable=False)

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

class Footer_Slider_section(db.Model):
    f_s_id=db.Column(db.Integer,primary_key=True,nullable=False)
    f_s_title=db.Column(db.String(50),nullable=False)
    f_s_description=db.Column(db.String(250),nullable=False)
    f_s_link=db.Column(db.String(250),nullable=False)
    f_s_link_title=db.Column(db.String(250),nullable=False) 
    f_s_image=db.Column(db.String(250),nullable=False)

class Owners_of_the_page_section(db.Model):
    own_id=db.Column(db.Integer,primary_key=True,nullable=False)
    own_title=db.Column(db.String(50),nullable=False)
    own_description=db.Column(db.String(250),nullable=False)
    own_image=db.Column(db.String(250),nullable=False)
    owner_posts=db.relationship('Posts',backref='Owners_of_the_page_section')


class Post_Categories(db.Model):
    p_c_id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_c_title=db.Column(db.String(50),nullable=False)
    p_c_description=db.Column(db.String(250),nullable=False)
    p_c_link=db.Column(db.String(250),nullable=False)
    p_c_link_title=db.Column(db.String(250),nullable=False) 
    p_c_image=db.Column(db.String(250),nullable=False)
    category_posts=db.relationship('Posts',backref='Post_Categories')

class Posts(db.Model):
    p_id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_title=db.Column(db.String(50),nullable=False)
    p_description=db.Column(db.Text,nullable=False)
    p_tags=db.Column(db.String(250),nullable=False)
    p_link=db.Column(db.String(250),nullable=False)
    p_image=db.Column(db.String(250),nullable=False)
    p_writer_id=db.Column(db.Integer, db.ForeignKey('Owners_of_the_page_section.own_id'),nullable=False)
    p_category_id=db.Column(db.Integer, db.ForeignKey('Post_Categories.p_c_id'),nullable=False)
    #post commentsde olmalidi amma hele prinsipi bilmediyim ucun yazmadim

    


  