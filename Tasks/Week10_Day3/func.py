import data
def AddUser(name,surname,idd):
    user={
        'Ad': name,
        'Soyad': surname,
        'Tam_ad': name+" "+surname,
        'id': idd
    }
    data.users.append(user)
    print("İstifadəçi müvəffəqiyyətlə əlavə edildi.")

