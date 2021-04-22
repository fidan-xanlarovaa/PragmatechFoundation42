import func
import data


n=int(input("Neçə istifadəçi daxil etmək istədiyinizi yazin:  "))
for i in range (n):
    name=input("Zəhmət olmasa istifadəçinin adını daxil edin:  ")
    surname=input("Zəhmət olmasa istifadəçinin soyadını daxil edin:  ")
    a=i
    func.AddUser(name,surname,a)

b=input("Daxil etdiyiniz məlumatlari görmək istəyirsinizmi? (Yes or No)  ")


if b=="Yes":
    print("Adlar:\t\tID:")
          
    for user in data.users:
        print(user['Tam_ad'] +"  |  "+ str(user['id']) )


