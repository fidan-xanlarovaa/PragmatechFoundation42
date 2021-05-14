#main

from flask import Flask,redirect,url_for,render_template,request
from app import app
from app.models import Motivation_word_section,About_section

@app.route("/")
def indexx():
    mottos=Motivation_word_section.query.all()
    about_sections=About_section.query.all()
    return render_template("main/index.html",mottos=mottos,about_sections=about_sections)



