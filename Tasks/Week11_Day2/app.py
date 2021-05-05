  
from typing import ClassVar
from flask import Flask,render_template,request,redirect
# asagida verilen route-larin icini tapsiriga uygun formada doldurmaq lazimdir

app=Flask(__name__)
myList=[]

def AddUser(name,surname,city):
    
    user={
        'Ad': name,
        'Soyad': surname,
        'Weher': city
    }
    myList.append(user) 

@app.route('/')
def index():     
    return render_template('index.html')
@app.route('/index')
def i():     
    return render_template('index.html')


@app.route('/add',methods=['GET','POST'])
def add():
    citys = ["Ağcabədi","Ağdam","Ağdaş","Ağdərə","Ağstafa","Ağsu","Astara","Babək","Bakı","Balakən","Beyləqan","Bərdə","Biləsuvar","Cəbrayıl","Cəlilabad","Culfa","Daşkəsən","Dəliməmmədli","Xocalı","Füzuli","Gədəbəy","Gəncə","Goranboy","Göyçay","Göygöl","Göytəpə","Hacıqabul","Horadiz","Xaçmaz","Xankəndi","Xocalı","Xocavənd","Xırdalan","Xızı","Xudat","İmişli","İsmayıllı","Kəlbəcər","Kürdəmir","Qax","Qazax","Qəbələ","Qobustan","Qovlar","Quba","Qubadlı","Qusar","Laçın","Lerik","Lənkəran","Liman",
    "Masallı","Mingəçevir","Naftalan","Naxçıvan","Neftçala","Oğuz","Ordubad","Saatlı","Sabirabad","Salyan","Samux","Siyəzən","Sumqayıt","Şabran","Şahbuz","Şamaxı","Şəki","Şəmkir","Şərur","Şirvan","Şuşa","Tərtər","Tovuz","Ucar","Yardımlı","Yevlax","Zaqatala","Zəngilan","Zərdab"
]
    if request.method=='POST':
        name=request.form['ad']
        surname=request.form['soyad']
        city=request.form['city']
        AddUser(name,surname,city)
        
    
    
    return render_template('add.html', citys=citys)



@app.route('/show')
def show():
    return render_template('show.html',data=myList)



if __name__=='__main__':
    app.run(debug=True)


    
