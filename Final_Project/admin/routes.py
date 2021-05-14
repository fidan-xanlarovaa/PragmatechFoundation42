#admin
from app import app
from app.models import *
from app import db
import os
from flask import render_template,redirect,request,url_for

### Admin panele giris hissesi

@app.route("/admin")
def index():
    return render_template("admin/index.html")


### Index.html about_section route

@app.route("/admin/about_s",methods=['POST','GET'])
def about_s():
    about_sections=About_section.query.all()
    if request.method=="POST":
        file=request.files['a_s_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        about_section=About_section(
            a_s_title=request.form["a_s_title"],
            a_s_description=request.form["a_s_description"],
            a_s_link=request.form["a_s_link"],
            a_s_link_title=request.form["a_s_link_title"],
            a_s_image=filename
        )
        db.session.add(about_section)
        db.session.commit()
        return redirect(url_for('about_s'))
    return render_template("admin/about_section.html",about_sections=about_sections)


### Index.html Motivation_word route

@app.route("/motivation_word_section",methods=['POST','GET'])
def motivation_word_s():
    m_w_descriptions=Motivation_word_section.query.all()
    if request.method=="POST":
        m_w=Motivation_word_section(
            m_w_description=request.form["m_w_description"]
            )
        db.session.add(m_w)
        db.session.commit()
        return redirect( url_for('motivation_word_s'))
    return render_template("admin/motivation_word_section.html", m_w_descriptions= m_w_descriptions)

 
        

