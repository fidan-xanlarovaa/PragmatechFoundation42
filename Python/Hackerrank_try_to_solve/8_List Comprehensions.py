from itertools import permutations 


__name__ = '__main__'
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
perm = permutations([x,y,z]) 

for i in list(perm): 
   
    if perm[0]+perm[1]+perm[2]:
        print (i)       
        
    
