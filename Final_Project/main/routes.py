#main 
# 
from flask import render_template,Flask,redirect,url_for,request
from app import app
from app.models import *


@app.route("/")
def indexx():
    mottos=Motivation_word_section.query.all()
    about_sections=About_section.query.all()
    owners=Owners_of_the_page_section.query.all()
    f_slider=Footer_Slider_section.query.all()
    slider=Slider_section.query.all()

    return render_template("main/index.html",mottos=mottos,about_sections=about_sections,owners=owners,f_slider=f_slider,slider=slider)



