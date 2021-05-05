from app import app
from app.models import Post
from app import db
import os
from flask import render_template,redirect,request


@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/news',methods=['GET','POST'])
def admin_news():
    posts=Post.query.all()
    if request.method=='POST':
        file=request.files['p_photo']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        post=Post(
            p_title=request.form['p_title'],
            p_desc=request.form['p_desc'],
            p_photo=filename
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/news')
    return render_template('admin/news.html',posts=posts)