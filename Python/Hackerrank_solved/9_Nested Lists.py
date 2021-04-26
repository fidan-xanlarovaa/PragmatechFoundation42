__name__ = '__main__'
list1 = []
if __name__ == '__main__':
    for a in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
#print(list1)
scorelist=[]
for i in list1:
    k=i[1]
    scorelist.append(k)
#print(scorelist)

scorelist.sort()
a=scorelist.pop(0)
scorelist[:] = (value for value in scorelist if value != a)
mini=min(scorelist)
#print(min(scorelist))

list1.sort()
for i in list1:
    if i[1]==mini:
       print(i[0])
