import data

def AddUser(name,surname,email,maas):
    
    user={
        'Ad': name,
        'Soyad': surname,
        'Tam_ad': name+" "+surname,
        
        'email': email,
        'maas':maas
    }
    data.users.append(user)
    
    print("\nİstifadəçi müvəffəqiyyətlə əlavə edildi.")
    

def EnSonElaveOLunan():
    a=data.users[-1]
    return a['Tam_ad']


def EnIlkElaveOLunan():
    a=data.users[0]
    return a['Tam_ad']
'''
def EnCoxMaasAlan():
    n=0
    maximum=data.users[0]
    
    for i in data.users:
        b=data.users[n]
        if i['maas']>b['maas']:
            maximum=data.users[i]
            return maximum['Tam_ad']
        n=n+1
 '''
def EnCoxMaasAlan():
    list2=[]
    for i in data.users:
        list2.append(i['maas'])
    maxi=max(list2)
    index=list2.index(maxi)
    max_user=data.users[index]
    return max_user['Tam_ad']
      


def MaaslarinCemi():
    summ=0
    for i in data.users:
        summ=summ+i['maas']
    return summ


def IstifadeciElaveEtmek():
    
    name=input("\nZəhmət olmasa işçinin adını daxil edin:  ")

    surname=input("Zəhmət olmasa işçinin soyadını daxil edin:  ")
    email=input("Zəhmət olmasa işçinin emailini daxil edin:  ")
    maas=int(input("Zəhmət olmasa işçinin maaşını daxil edin:  "))
    
    AddUser(name,surname,email,maas)
    