import math

def is_leap(year):
    leap = False
    
    if math.remainder(year,4)==0 :
        leap=True
        if math.remainder(year,100)==0:
            leap = False
            if  math.remainder(year,400)==0:
                leap=True
                

    
    return leap

year = int(input())