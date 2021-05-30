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

class Owner_Form(FlaskForm):
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

class Category_Form(FlaskForm):
    p_c_title=StringField('p_c_title',render_kw={"placeholder": "Kateqoriyanın başlığını əlavə edin"})
    p_c_description=StringField('p_c_description',render_kw={"placeholder":"Kateqoriya üçün əlavə məlumatı daxil edin"})
    p_c_link=StringField('p_c_link',render_kw={"placeholder":"Kateqoriyanın düymə linkini daxil edin"})
    p_c_link_title=StringField('p_c_link_title',render_kw={"placeholder":"Kateqoriyanın düymə başlığını əlavə edin"})
    p_c_image=FileField('p_c_image')
    submit=SubmitField() 
    
class Prcategory_Form(FlaskForm):
    p_r_c_title=StringField('p_r_c_title',render_kw={"placeholder": "Kateqoriyanın başlığını əlavə edin"})
    p_r_c_description=StringField('p_r_c_description',render_kw={"placeholder":"Kateqoriya üçün əlavə məlumatı daxil edin"})
    p_r_c_link=StringField('p_r_c_link',render_kw={"placeholder":"Kateqoriyanın düymə linkini daxil edin"})
    p_r_c_link_title=StringField('p_r_c_link_title',render_kw={"placeholder":"Kateqoriyanın düymə başlığını əlavə edin"})
    p_r_c_image=FileField('p_c_image')
    submit=SubmitField() 


    


    





