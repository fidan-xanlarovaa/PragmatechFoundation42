from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,validators

class CategoryForm(FlaskForm):
    cat_name=StringField('cat_name',[validators.Length(min=8, max=25,message='Melumat duz deyil')])
    submit=SubmitField()

class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    cat_name=db.Column(db.String(50))


@app.route('/admin/kategoriya/',methods=['GET','POST'])
def admin_category():
    form=CategoryForm()
    categories=Category.query.all()
    if request.method=='POST':
        category=Category(
                cat_name=form.cat_name.data
            )
        db.session.add(category)
        db.session.commit()
        if form.validate():
            pass  
        else:
            flash('Duzgun melumat deyil')
        return redirect(url_for('admin_category'))
        
    return render_template('admin/category.html',form=form,categories=categories) 
© 2021 GitHub, Inc.




{% extends "admin/base.html" %} {% block content %}
<h3 class="my-2">Kategoriya Bölməsi</h3>
<hr>
<h5 class="my-3"> Yeni Kategoriya</h5>

<form action="{{url_for('admin_category')}}" method='POST' enctype="multipart/form-data">
    {{ form.cat_name(class='form-control my-2') }} {{ form.submit(value='Add Category',class='btn btn-primary')}}
</form>

<div class="alert alert-danger" role="alert">
    {{message}}
</div>

<hr>
<h5 class="my-3"> Bütün Kategoriyalar</h5>
<table class="table">
    <thead>
        <tr>
            <th>Kategoriya adi</th>
            <th></th>
        </tr>
    </thead>
    <tbody>

        {% for category in categories %}
        <tr>
            <td scope="row">{{category.cat_name}}</td>
            <td>
                <a href="">Sil</a>
                <a href="">Yenilə</a>
            </td>
        </tr>
        {% endfor %}


    </tbody>
</table>
{% endblock %}