#from itertools import permutations 


#__name__ = '__main__'
##   x = int(input())
 #   y = int(input())
  #  z = int(input())
  #  n = int(input())
#perm = permutations([x,y,z]) 

#for i in list(perm): 
   
 #   print (i)       
'''
__name__ = '__main__'
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
print(list(arr))'''

__name__ = '__main__'
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()[:n])
list1=list(arr)

list1.sort()
a=list1.pop(-1)
for i in list1:
    if i==a:
        list1.remove(i)
print(list1)

