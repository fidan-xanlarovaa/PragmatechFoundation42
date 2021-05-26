from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,validators
from wtforms.fields.core import SelectMultipleField
from app.models import *
from app import db

class Footer_Slider_section_Form(FlaskForm):
    f_s_title=StringField('f_s_title',render_kw={"placeholder": "Sliderin başlığını əlavə edin"})
    f_s_description=StringField('f_s_description',render_kw={"placeholder":"Slider üçün əlavə məlumatı daxil edin"})
    f_s_link=StringField('f_s_link',render_kw={"placeholder":"Sliderin düymə başlığını əlavə edin"})
    f_s_link_title=StringField('f_s_link_title',render_kw={"placeholder":"Slider  düymə linkini daxil edin"})
    f_s_image=FileField('f_s_image')
    submit=SubmitField()

class Owners_of_the_page_section_Form(FlaskForm):
    own_title=StringField('own_title',render_kw={"placeholder": "Adminin ad və soyadını daxil edin"})
    own_description=StringField('own_description',render_kw={"placeholder": "Admin haqqında əlavə məlumatı daxil edin"})
    own_image=FileField('own_image')
    submit=SubmitField()

class Slider_section_Form(FlaskForm):
    s_title=StringField('s_title',render_kw={"placeholder": "Sliderin başlığını əlavə edin"})
    s_description=StringField('s_description',render_kw={"placeholder":"Slider üçün əlavə məlumatı daxil edin"})
    s_link=StringField('s_link',render_kw={"placeholder":"Sliderin düymə başlığını əlavə edin"})
    s_link_title=StringField('s_link_title',render_kw={"placeholder":"Slider  düymə linkini daxil edin"})
    s_image=FileField('s_image')
    submit=SubmitField() 

class Post_Categories_Form(FlaskForm):
    p_c_title=db.Column(db.String(50),nullable=False)
    p_c_description=db.Column(db.String(250),nullable=False)
    p_c_link=db.Column(db.String(250),nullable=False)
    p_c_link_title=db.Column(db.String(250),nullable=False) 
    p_c_image=db.Column(db.String(250),nullable=False)
    category_posts=db.relationship('Posts',backref='Post_Categories')

class Posts_Form(FlaskForm):
    #choices=Post_Categories.query.filter_by()
    p_title=StringField('p_title',render_kw={"placeholder":"Post başlığını daxil edin"})
    p_description=StringField('p_description',render_kw={"placeholder":"Postun məzmununu daxil edin"})
    p_tags=StringField('p_tags',render_kw={"placeholder":"Postun məzmununu daxil edin"})
    p_link=StringField('p_link',render_kw={"placeholder":"Postun məzmununu daxil edin"})
    p_image=StringField('p_image')
    #p_writer_id=SelectMultipleField('p_writer_id',choices=[])
    #SelectMultipleField(choices = my_choices, default = ['1', '3'])
    #p_category_id=db.Column(db.Integer, db.ForeignKey('Post_Categories.p_c_id'),nullable=False)
    #post commentsde olmalidi amma hele prinsipi bilmediyim ucun yazmadim

    


    





