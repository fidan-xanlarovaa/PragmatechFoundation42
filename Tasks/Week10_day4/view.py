import func
import data



    

# b=input("Daxil etdiyiniz məlumatlari görmək istəyirsinizmi? (Yes or No)  ")

'''
if b=="Yes":
    print("Adlar:\t\tID:")
          
   


'''

w=True
print("\n\n--Salam mini HR proqramına xoş gəlmisiniz--\n")
while w==True:
    emr=input("\n\nZəhmət olmasa sizə uyğun əmri seçin:\n\nYeni işçi əlavə etmək üçün _ 1\tİstifadəçi məlumatlarına baxmaq üçün _ 2\tÜmumi maaş cəmini göstər üçün _ 3\tİşçi sayını göstərmək üçün _ 4\n\nƏn köhnə işçini göstərmək üçün _ 5\tƏn yeni işçini göstərmək üçün _ 6\tƏn çox maaş alan işçini görmək üçün _ 7\tƏsas menyuya qayıtmaq, yəni prosesi sonlandırmaq  üçün _ 8\n\nDüyməsini seçin !  ")
    if emr=="1":
        func.IstifadeciElaveEtmek()
    
    elif emr=="2":
        
        for user in data.users:
            print("\n"+user['Tam_ad'] +"  |  "+ user['email']+"  |  "+ str(user['maas']))
    elif emr=="3":
        print("\nBüdcədən işcilərin maaşı üçün ayrılan məbləğ " + str(func.MaaslarinCemi())+" manat təşkil edir.")
    elif emr=="4":
        print("\nBizim şirkətin işçi kollektivi "+ str(len(data.users)) + " nəfərdən ibarətdir.")
    elif emr=="5":
        print("\nBizim şirkətdə ən çox təcrübəyə malik işçinin ad və soyadını sizə təqdim edirik: "+ func.EnIlkElaveOLunan())
    elif emr=="6":
        print("\nBizim şirkətin ən yeni işçisinin ad və soyadını sizə təqdim edirik: "+func.EnSonElaveOLunan())
    elif emr=="7":
        print("\nBizim şirkətin ən çox maaş alan işçisinin ad və soyadını sizə təqdim edirik: \n"+func.EnCoxMaasAlan())
    elif emr=="8":
        w=False
        print("\nBizi seçdiyiniz üçün təşəkkür edirik !")
    else:
        print("\nDaxil etdiyiniz sorğuya uyğun nəticə tapılmadı, zəhmət olmasa əmrlər siyahısından sizə uyğun əmri seçin ! Əmrlərin nömrəsini daxil edərkən sağında və ya solunda heç bir simvol və boşluq qoymadığınızdan əmin olun !  ")


# "\nBizim şirkətdə ən çox maaş alan işçinin ad və soyadını sizə təqdim edirik: "




