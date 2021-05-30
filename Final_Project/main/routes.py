#main 
# 
from flask import render_template,Flask,redirect,url_for,request
from app import app
from app.models import *


@app.route("/")
def indexx():
    mottos=Motivation_word_section.query.all()
    about_sections=About_section.query.all()
    owners=Owner.query.all()
    f_slider=Footer_Slider_section.query.all()
    slider=Slider_section.query.all()
    pr_categories=Prcategory.query.all()

    """ 
    postNum=len(Posts)
    postss=Posts.query.all()
    post1=postss[postNum-1]
    post2=postss[postNum-2]
    post3=postss[postNum-3]"""
  

    return render_template("main/index.html",mottos=mottos,about_sections=about_sections,owners=owners,f_slider=f_slider,slider=slider,pr_categories=pr_categories )
    #""", post1= post1, post2= post2, post3= post3"""

@app.route("/about")
def about():
    categories=Category.query.all()
    cate1=categories[0]
    cate2=categories[1]
    cate3=categories[2]

    return render_template("main/about.html",cate1=cate1,cate2=cate2,cate3=cate3)

@app.route("/productss")
def productss():
    
    productsy=Products.query.all()
    
    
    return render_template("main/postlarKateqoriyali.html",productsy=productsy)



@app.route("/products_hair")
def products_hair():
    
    productsy=Products.query.filter_by(prcategory_id = "Saç üçün məhsullar").all()
    
    
    return render_template("main/mehsulsac.html",productsy=productsy)


@app.route("/products_hair")
def products_skin():
    
    productsy=Products.query.filter_by(prcategory_id = "Üz üçün məhsullar").all()
    
    
    return render_template("main/mehsulderi.html",productsy=productsy)


