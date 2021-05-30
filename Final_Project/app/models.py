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

class Owner(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    own_title=db.Column(db.String(50),nullable=False)
    own_description=db.Column(db.String(250),nullable=False)
    own_image=db.Column(db.String(250),nullable=False)
    posts=db.relationship('Posts', backref='owner', lazy=True)


class Category(db.Model):
    
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_c_title=db.Column(db.String(50),nullable=False)
    p_c_description=db.Column(db.String(250),nullable=False)
    p_c_link=db.Column(db.String(250),nullable=False)
    p_c_link_title=db.Column(db.String(250),nullable=False) 
    p_c_image=db.Column(db.String(250),nullable=False)
    posts=db.relationship('Posts', backref='category', lazy=True)

class Posts(db.Model):
    
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_title=db.Column(db.String(50),nullable=False)
    p_description=db.Column(db.Text,nullable=False)
    p_data= db.Column(db.DateTime)
    p_tags=db.Column(db.String(250),nullable=False)
    p_link=db.Column(db.String(250),nullable=False)
    p_image=db.Column(db.String(250),nullable=False)
    owner_id=db.Column(db.Integer,db.ForeignKey('owner.id'),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    #post commentsde olmalidi amma hele prinsipi bilmediyim ucun yazmadim

class Prcategory(db.Model):
    
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_r_c_title=db.Column(db.String(50),nullable=False)
    p_r_c_description=db.Column(db.String(250),nullable=False)
    p_r_c_link=db.Column(db.String(250),nullable=False)
    p_r_c_link_title=db.Column(db.String(250),nullable=False) 
    p_r_c_image=db.Column(db.String(250),nullable=False)
    products=db.relationship('Products', backref='prcategory', lazy=True)

class Products(db.Model):
    
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    p_r_title=db.Column(db.String(50),nullable=False)
    p_r_description=db.Column(db.Text,nullable=False)
    
    p_r_price=db.Column(db.String(250),nullable=False)
    p_r_image=db.Column(db.String(250),nullable=False)
    prcategory_id=db.Column(db.Integer,db.ForeignKey('prcategory.id'),nullable=False)

