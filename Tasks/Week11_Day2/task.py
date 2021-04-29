  
from typing import ClassVar
from flask import Flask,render_template,request,redirect
# asagida verilen route-larin icini tapsiriga uygun formada doldurmaq lazimdir

task=Flask(__name__)
myList=[]

@app.route('/')
def index():
    
        
    return render_template('index.html')


@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        name=request.form['ad']
        surname=request.['soyad']
        city=request.['Weher']
        AddUser(name,surname,city)
    return render_template('add.html')


@app.route('/show')
def show():
    
    return render_template('show.html',data=myList)

if __name__=='__main__':
    task.run(debug=True)

def AddUser(name,surname,city):
    
    user={
        'Ad': name,
        'Soyad': surname,
        'Weher': city
    }
    myList.append(user)
    
