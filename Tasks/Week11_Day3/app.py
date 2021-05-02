from typing import ClassVar
from flask import Flask,render_template,request,redirect

app=Flask(__name__)
myUsers=[]
id=1

@app.route('/',methods=['GET','POST'])
def index():
    global id
    if request.method=="POST":
        user={
            'id':id,
            'name':request.form['ad'],
            'surname':request.form['soyad']
        }
        myUsers.append(user)
        id=id+1
        return redirect("/shw")
    return render_template("index.html")

@app.route("/shw")
def shw():
    return render_template("shw.html",myUsers=myUsers)

@app.route("/delete/<silinicekId>")
def delete(silinecekId):
    for user in users:
        if user['id']==int(silinecekId):
            myUsers.remove(user)
            return redirect("/shw")


@app.route("/update/<Id>")
def update(Id):
    for user in users:
        if user['id']==int(Id):
             user={
            'id':Id,
            'name':request.form['ad'],
            'surname':request.form['soyad']
            }
        return redirect("/shw")


if __name__=='__main__':
    app.run(debug=True)


